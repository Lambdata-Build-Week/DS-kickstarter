# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import dash_design_kit as ddk
import dash_daq as daq

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Predictions

            How much are you looking to raise for your project?

            """
        ),

        dcc.Slider(
            id='slider1',
            min=0,
            max=50000,
            step=100,
            value=5000,
            marks={0: '0',
                   10000: '$10000',
                   20000: '$20000',
                   30000: '$30000',
                   40000: '$40000',
                   50000: '$50000'},
            className='mb-3'  # this gives margin spacing to the bottom
        ),

        dcc.Markdown("", id='output1',
                     className='mb-5'),

        dcc.Markdown("What category does your project fall under?"),

        dcc.Dropdown(
            options=[
                {'label': 'Digital Art', 'value': 'Digital Art'},
                {'label': '3D Printing', 'value': '3D Printing'},
                {'label': 'Mixed Media', 'value': 'Farms'},
                {'label': 'People', 'value': 'People'},
                {'label': 'Web', 'value': 'Web'},
                {'label': 'Photobooks', 'value': 'Photobooks'},
                {'label': 'Animals', 'value': 'Animals'},
                {'label': 'Rock', 'value': 'Rock'},
                {'label': 'Graphic Novels', 'value': 'Graphic Novels'}
            ],
            placeholder="Select a Category",
            className='mb-5'
        ),

        dcc.Markdown("How many days will your project be open for funding?"),

        dcc.Slider(
            id='slider2',
            min=0,
            max=60,
            step=1,
            marks={
                0: '0',
                10: '10 days',
                20: '20 days',
                30: '30 days',
                40: '40 days',
                50: '50 days',
                60: '60+ days'
            },
            value=30,
            className='mb-3'
        ),

        dcc.Markdown("", id='output2',
                     className='mb-5'),

        dcc.Markdown("What month will you be launching your project?"),

        dcc.Dropdown(
            options=[
                {'label': 'January', 'value': 'January'},
                {'label': 'February', 'value': 'February'},
                {'label': 'March', 'value': 'March'},
                {'label': 'April', 'value': 'April'},
                {'label': 'May', 'value': 'May'},
                {'label': 'June', 'value': 'June'},
                {'label': 'July', 'value': 'July'},
                {'label': 'August', 'value': 'August'},
                {'label': 'September', 'value': 'September'},
                {'label': 'October', 'value': 'October'},
                {'label': 'November', 'value': 'November'},
                {'label': 'December', 'value': 'December'},
            ],
            placeholder="Select a Month",
            className='mb-5'

)  

    ],
    md=6,
)

column2 = dbc.Col(
       className='mb-50'

)

column3 = dbc.Col(
    [
        dcc.Markdown(
            """
            Given the selected features of your project,
            your chance of success is:
            """
        ),

        daq.Gauge(
        id ='my-daq-gauge',
        min =0,
        max =100,
        value =80),

        dcc.Markdown(
            """
            More text options to be added later.
            """
        ),


    ],
    className='mb-50',
    md=4,
)

layout = dbc.Row([column1, column2, column3])


@app.callback(
    Output(component_id='output1', component_property='children'),
    [Input(component_id='slider1', component_property='value')]
)
def update_output_div(input_value):
    return '***You have selected to raise: ${} ***'.format(input_value)


@app.callback(
    Output(component_id='output2', component_property='children'),
    [Input(component_id='slider2', component_property='value')]
)
def update_output_div2(input_value):
    return '***Your project will be open {} days for funding***'.format(input_value)
