import pytest
from unittest.mock import Mock, patch
from utils import (
    MeteoCity,
    degrees_to_cardinal,
    process_form,
)


@pytest.fixture
def meteocity_instance():
    return MeteoCity()

def test_get_coordinates(meteocity_instance):
    with patch('geopy.geocoders.Nominatim.geocode') as mock_geocode:
        mock_geocode.return_value.latitude = 48.85341
        mock_geocode.return_value.longitude = 2.3488

        coordinates = meteocity_instance.get_coordinates("Paris")
        assert coordinates == (48.85341, 2.3488)

def test_build_url(meteocity_instance):
    coordinates = (48.85341, 2.3488)
    url = meteocity_instance.build_url(coordinates)

    expected_url = f"http://www.infoclimat.fr/public-api/gfs/json?_ll={coordinates[0]},{coordinates[1]}&_auth=BR8AFwN9UXNec1ZhD3kBKFgwBzIJf1B3VCgBYghtVCkDaAVkBmYEYlU7UC0DLAcxVXhUNwA7AzNUPwZ%2BDnxUNQVvAGwDaFE2XjFWMw8gASpYdgdmCSlQd1Q0AWEIe1Q2A2cFYQZ7BGdVM1AsAzIHO1VnVCsAIAM6VDAGYQ5hVDMFYQBlA2RRO141VisPIAEzWG4HYAk%2FUDlUMAFlCDZUMANlBWUGZwRjVTxQLAMxBzdVb1QzAD4DM1Q2BmIOfFQoBR8AFwN9UXNec1ZhD3kBKFg%2BBzkJYg%3D%3D&_c=a4e326c9002d3da1f27b05278ec29d55"
    
    assert url == expected_url

# Using the xfail decorator as the API has a very low rate limit, hence often throwing an error
@pytest.mark.xfail(reason="Geocoding service is unavailable")
def test_query(meteocity_instance):
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {'temperature': 25, 'humidity': 80}
        mock_get.return_value = mock_response

        results = meteocity_instance.query("Paris")

        assert results == {'temperature': 25, 'humidity': 80}

def test_degrees_to_cardinal():
    assert degrees_to_cardinal(0) == 'N'
    assert degrees_to_cardinal(45) == 'NE'
    assert degrees_to_cardinal(90) == 'E'
    assert degrees_to_cardinal(135) == 'SE'
    assert degrees_to_cardinal(180) == 'S'
    assert degrees_to_cardinal(225) == 'SW'
    assert degrees_to_cardinal(270) == 'W'
    assert degrees_to_cardinal(315) == 'NW'
    assert degrees_to_cardinal(360) == 'N'
    assert degrees_to_cardinal(405) == 'NE'

def test_city_name_assertion():
    with pytest.raises(AssertionError) as e:
        process_form(123, 6)
    assert str(e.value) == "City name must be a string"

def test_horizon_assertion():
    with pytest.raises(AssertionError) as e:
        process_form("Paris", "test")
    assert str(e.value) == "Horizon must be a strictly positive integer"