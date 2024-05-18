# Imports 
import dash
import pandas as pd 
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash import html, dcc, Input, Output, callback, dash_table, Dash


# Self-defined 
# from graph import feature_plots
# from maps import biomass_fig
meta_tags = [
            {"name": "viewport",
            "content": "width=device-width, initial-scale=1"}
    ]

# Set up stylesheets 
static_css = 'assets/style.css'
stylesheets = [static_css, dbc.themes.DARKLY, dbc.icons.FONT_AWESOME]
# Load data once
data_dir = "./data/trawlers.csv"
df = pd.read_csv(data_dir)

# Get a list of attributes to display 
column_list = ["Speed", "Heading", "Avg. Heading"]
attr_list = [column for column in df.columns if column in column_list]

# Register page 
dash.register_page(__name__, top_nav = True, name = 'Table')

# Instantiate app 
# app = Dash(__name__, meta_tags = meta_tags, external_stylesheets = stylesheets)

# Define the navbar
navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.NavbarBrand("Home", href="/", id = 'home-bar', style={'color': 'white'})
            ], id = "nav-bar")
        ], align="center", className="flex-grow-1", style = {"left": 0}),
        dbc.Row([
        ], className="g-0 ms-auto flex-nowrap mt-3 mt-md-0", align="center"),
    ]),
    dark = False,
    fixed = "top",
    style = {"padding": '30px 0px'},
)

layout = html.Div([
    dbc.Container([
        navbar,
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Label(''),
        dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], 
                         id='tbl', page_size = 20, style_table = {"color": 'black','fontFamily': 'sans-serif','fontSize': 12}),
        dbc.Alert(id= 'tbl_out'),
    ])
])
# # App layout
# layout = dbc.Container([
#     dbc.Label('Click a cell in the table:'),
#     dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], 
#                          id='tbl', page_size = 20, style_table = {"color": 'black','fontFamily': 'sans-serif','fontSize': 12}),
#     dbc.Alert(id= 'tbl_out'),
# ])

@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"
