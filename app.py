# Imports 
import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

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


# Instantiate app 
app = Dash(__name__, meta_tags = meta_tags, external_stylesheets = stylesheets, use_pages = True, pages_folder = 'pages')

# Set up favicon 
app._favicon = './assets/fish.png'

# Set up server 
server = app.server 

# Define the layout of the app
app.layout = html.Div([
    dash.page_container
])


if __name__ == '__main__':
    app.run()

