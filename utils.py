import requests
from geopy.geocoders import Nominatim
from typing import Tuple, Iterable, Dict, Union

from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import linear_cmap
from bokeh.embed import components
from bokeh.resources import CDN
import pandas as pd
import datetime

class MeteoCity:
    def __init__(self) -> None:
        self.base_url = 'http://www.infoclimat.fr/public-api/gfs/json?_ll='
        
    def get_coordinates(self, location: str) -> Tuple[float, float]:
        geolocator = Nominatim(user_agent="my_own_app")
        city = geolocator.geocode(location)
        return city.latitude, city.longitude

    def build_url(self, coordinates: Iterable) -> str:
        return f"{self.base_url}{coordinates[0]},{coordinates[1]}&_auth=BR8AFwN9UXNec1ZhD3kBKFgwBzIJf1B3VCgBYghtVCkDaAVkBmYEYlU7UC0DLAcxVXhUNwA7AzNUPwZ%2BDnxUNQVvAGwDaFE2XjFWMw8gASpYdgdmCSlQd1Q0AWEIe1Q2A2cFYQZ7BGdVM1AsAzIHO1VnVCsAIAM6VDAGYQ5hVDMFYQBlA2RRO141VisPIAEzWG4HYAk%2FUDlUMAFlCDZUMANlBWUGZwRjVTxQLAMxBzdVb1QzAD4DM1Q2BmIOfFQoBR8AFwN9UXNec1ZhD3kBKFg%2BBzkJYg%3D%3D&_c=a4e326c9002d3da1f27b05278ec29d55"

    def query(self, location=None) -> Dict:
        coordinates = self.get_coordinates(location)
        full_url = self.build_url(coordinates)
        response = requests.get(full_url)
        results = response.json()
        return results

def degrees_to_cardinal(degrees: Union[float, int]) -> str:
    """
    Convert a given angle in degrees to the corresponding cardinal direction.

    Parameters:
    - degrees (float or int): The angle in degrees to be converted into a cardinal direction.
                              The valid range is typically 0 to 360, representing a full circle.

    Returns:
    - str: The cardinal direction corresponding to the input angle.
           Returns one of the eight cardinal directions: 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'.      
    """
    
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    index = round(degrees / 45) % 8
    return directions[index]

def process_form(city_name: str, horizon: int = 6) -> pd.DataFrame:
    """
    Process weather information for a specified city and return the data in a DataFrame.

    Parameters:
    - city_name (str): The name of the city for which weather information is requested.
                        Note: city must be located in France
    - horizon (int): Number of forecast days to retrieve weather data for. Default is 6.

    Returns:
    - pd.DataFrame: Processed weather data for the specified number of days.
    """

    assert isinstance(city_name, str), "City name must be a string"
    assert isinstance(horizon, int) and horizon > 0, "Horizon must be a strictly positive integer"

    # Query weather information for the specified city
    meteocity = MeteoCity()
    result = meteocity.query(location=city_name)

    # Get dates for the next 'horizon' days
    today = datetime.date.today()
    dates = [str(today + datetime.timedelta(days=i)) for i in range(horizon)]

    # Filter out relevant data for the next 'horizon' days
    filtered_data = {
        key: value for (key, value) in result.items() 
        if any(day in key for day in dates) and "-" in key
    }

    # Convert the filtered dictionary to a DataFrame
    df = pd.DataFrame.from_dict(filtered_data, orient='index')

    # Convert index to datetime
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d %H:%M:%S')

    # Create 'Day' column
    df['Day'] = df.index.day

    # Create 'Hour' column
    df['Hour'] = df.index.strftime('%Hh')

    # Convert temperature from Kelvin to Celsius
    df['Temperature'] = df['temperature'].apply(lambda x: round(x.get('2m') - 273.15, 1))

    return df


def create_bokeh_plots(df: pd.DataFrame) -> Tuple[str, str, str, str]:
    """
    Create Bokeh plots for temperature variation over days.

    Parameters:
    - df (pd.DataFrame): Processed weather data for the next six days.

    Returns:
    - Tuple[str, str, str, str, str]: A tuple containing the following elements:
        - script (str): JavaScript code for rendering Bokeh plots.
        - div (str): HTML code representing the Bokeh plots.
        - cdn_js (str): CDN JavaScript code for Bokeh.
        - widget_js (str): JavaScript code for Bokeh widgets.
        - resources (str): CDN resources for Bokeh.
    """

    plots = []

    for date, date_group in df.groupby(['Day']):
        wind_values = [f"{value['10m']}km/h {degrees_to_cardinal(value['10m'])}" for value in date_group.vent_moyen.values]
        humidity_values = [f"{value['2m']}%" for value in date_group.humidite]

        df_day = pd.DataFrame({
            'Hour': date_group.Hour.values,
            'Temperature': date_group.Temperature.values,
            'Rain': date_group.pluie.values,
            'Wind': wind_values,
            'Humidity': humidity_values,
            'Risk_Snow': date_group.risque_neige.values
        })

        date = date_group.index[0]
        date_formatting = '%A, %d. %B %Y' 
        date = date.strftime(date_formatting)

        source = ColumnDataSource(df_day)
        plot = figure(width=400,
                      height=300,
                      title=date,
                      x_range=df_day.Hour.unique(),
                      tools='tap')

        TOOLTIPS = [
            ("Temperature", "@Temperature{00}°C"),
            ("Rain", "@Rain{0.0}mm"),
            ("Wind", "@Wind"),
            ("Humidity", "@Humidity"),
            ("Snow Chance", "@Risk_Snow")
        ]
        plot.add_tools(HoverTool(tooltips=TOOLTIPS))

        cmap = linear_cmap(
            field_name='Temperature',
            palette='Viridis256',
            low=min(df_day.Temperature),
            high=max(df_day.Temperature)
        )

        plot.line(x='Hour',
                  y='Temperature',
                  width=1,
                  color='darkgray',
                  source=source)

        plot.scatter(x='Hour',
                     y='Temperature',
                     color=cmap,
                     size=8,
                     source=source)

        plot.grid.grid_line_alpha = 0.0
        plot.axis.minor_tick_out = 0
        plot.yaxis.major_tick_out = 3
        plot.toolbar.logo = None
        plot.background_fill_color = '#FFFFFF' # Could have been: plot.background_fill_color = None
        plot.background_fill_alpha = 0.1
        plot.axis.axis_label_text_font_size = '16px'
        plot.axis.major_label_text_font_size = "16px"
        plot.border_fill_color = None
        plot.toolbar_location = None
        plot.outline_line_color = None
        plot.yaxis.axis_label = 'Temperature (°C)'
        # plot.xaxis.axis_label = 'Hour'
        plots.append(plot)

    grid = gridplot(plots,
                    ncols=3,
                    width=450,
                    height=280)
    grid.toolbar_location = None
    script, div = components(grid)
    # Get both CDN & widget JavaScript code
    cdn_js, widget_js = CDN.js_files[0], CDN.js_files[2]
    resources = CDN.render()

    return script, div, cdn_js, widget_js, resources