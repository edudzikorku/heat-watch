# Imports 
import dash
from dash import html

# Register page 
dash.register_page(__name__, path = '/', top_nav = True)

# Define the layout
layout = html.Div([
    html.Video(
        src = "/assets/trawler_2.mp4", 
        autoPlay = True,
        muted = True,
        loop = True,
        id = "myVideo",
    ),
    
    html.Div([
        html.Div([
            html.Main([
                html.Div([
                    html.H1([
                        html.Strong("MarineHeat"),
                        " | Monitoring Trawler Activity"
                    ]),
                    html.H2("Visualizing Tuna Fishing Zones"),
                    html.A([
                        html.Span("Open App")
                    ], href = "/heatmap"),
                    html.A([
                        html.Span("Get Data")
                    ], href = "https://github.com/edudzikorku/heat-watch/tree/main/data")
                ], id = "index-info")
            ], className = "d-flex h-100 w-100 justify-content-center align-items-center")
        ], id = "index-overlay")
    ], id = "index-bg")
])