# Imports 
import dash
import pandas as pd 
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash import html, dcc, Input, Output, callback

# Load data once
data_dir = "./data/trawlers.csv"
df = pd.read_csv(data_dir)

# Get a list of attributes to display 
column_list = ["Speed", "Heading", "Avg. Heading"]
attr_list = [column for column in df.columns if column in column_list]

# Register page 
dash.register_page(__name__, top_nav = True, name = 'Series')

# Function to create initial empty figure
def initial_fig():
    scatter_mapbox_trace = go.Scattermapbox()

    # Define the layout for the map
    layout = go.Layout(
        mapbox=dict(
            style = "open-street-map", 
            center = dict(lon = -0.1852226, lat = 5.4839085),
            zoom = 8,
            bearing = 0,
            pitch = 0,
        ),
    )
    # Create the figure
    fig = go.Figure(data=[scatter_mapbox_trace], layout=layout)
    fig.update_layout(margin = {"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

# Define four empty figures for the inset maps
inset_fig1 = initial_fig()

# Define the navbar
navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.NavbarBrand("Home", href="/", id = 'home-bar', style={'color': 'white'})
            ], id = "nav-bar")
        ], align="center", className="flex-grow-1", style = {"left": 0}),
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(id='inset',
                             value=attr_list[1],
                             options=[{'label': attr, 'value': attr} for attr in attr_list],
                             placeholder="Select an attribute",
                             style={'fontFamily': 'sans-serif', 'color': 'black', 'width': '100%'}
                             )
            ], width=4, style={'minWidth': '200px'}) 
        ], className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),
    ]),
    dark = False,
    fixed = "top",
)

# App layout
layout = html.Div([
    dbc.Container([
        navbar,
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='heat-map-animation',
                          figure = inset_fig1,
                          config = {'displayModeBar': False},
                          style = {'height': '90vh'}
                          )
            ], style={'height': '90vh'})
        ], style={'height': '90vh', 'marginTop': '56px'}) 
    ], fluid=True, style={'padding': '20px 0 0 0', 'margin': 0, 'height': '40%'}), 
],
)


# Define the callback
@callback(
    Output('heat-map-animation', 'figure'),
    Input('inset', 'value'),
    allow_duplicate = True
)
def displayHeatMap(attr):
    # Create the updated figure
    fig = px.density_mapbox(df, lat = 'Latitude', lon = 'Longitude', z = attr, radius = 10,
                            center=dict(lat = 5.4839085, lon = -0.1852226), zoom = 10,
                            mapbox_style = "open-street-map", animation_frame = "Date"
                            )
    # Update figure layout
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      coloraxis_colorbar = dict(orientation = 'h', yanchor = 'bottom', y = -0.1))

    return fig

