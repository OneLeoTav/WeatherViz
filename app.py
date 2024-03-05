from flask import Flask, render_template, request
from utils import process_form, create_bokeh_plots

import pytest


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If the form is submitted, get the city from the form
        city_name = request.form.get('city', '')
        df = process_form(
                city_name=city_name,
                horizon=6,
            )
        
        script, div, cdn_js, widget_js, resources = create_bokeh_plots(df)

        return render_template('index.html',
                               script=script,
                               div=div,
                               cdn_js=cdn_js,
                               widget_js=widget_js,
                               resources=resources,
                               city_name=city_name)
    else:
        # Default city if not submitted
        city_name = "Paris"
        return render_template('index.html', city_name=city_name)

if __name__ == '__main__':
    pytest.main(['-v', 'tests.py'])
    app.run(host='0.0.0.0', port=8080, debug=True)
    
# if __name__ == '__main__':
#     # Run tests
#     result_code = pytest.main(['-v', 'tests.py'])
    
#     # Start the application if - and only if - all tests pass
#     if result_code == 0:
#         app.run(host='0.0.0.0', port=8080, debug=True)
#     else:
#         print("Tests failed. Application not started.")    