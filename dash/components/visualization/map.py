# dash imports
import plotly.express as px
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from dash import State
from scipy.stats import probplot
import plotly.graph_objs as go

# file imports
from maindash import my_app
from utils.file_operation import read_file_as_str

# import the dataset
url = "https://raw.githubusercontent.com/mnguyen0226/two_sigma_property_listing/main/data/train.json"
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]


def map_layout():
    layout = html.Div(
        [
            dcc.Loading(
                children=[dcc.Graph(id="visualization_map_heatmap")], type="circle"
            ),
        ]
    )
    return layout


def map_content():
    return html.Div(
        [
            html.Div([html.H3("🎛 Tune")]),
            html.Div(
                [
                    dcc.Dropdown(
                        id="visualization_map_dropdown",
                        options=[
                            {"label": "High Interest", "value": "high"},
                            {"label": "Medium Interest", "value": "medium"},
                            {"label": "Low Interest", "value": "low"},
                        ],
                        value="high",
                    ),
                ]
            ),
        ]
    )


@my_app.callback(
    Output("visualization_map_heatmap", "figure"),
    [Input("visualization_map_dropdown", "value")],
)
def update_heatmap(selected_interest):
    filtered_data = df_filtered[df_filtered["interest_level"] == selected_interest]
    fig = px.density_mapbox(
        filtered_data,
        lat="latitude",
        lon="longitude",
        z="price",
        radius=8,
        center=dict(lat=40.7128, lon=-74.0060),  # center on NYC
        zoom=9, 
        mapbox_style="open-street-map",
    )

    fig.update_layout(
        title={
            "text": f"Heatmap of NYC Rental Listings - {selected_interest.capitalize()} Interest",
            "x": 0.5,
            "xanchor": "center",
        }
    )

    return fig


def map_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="visualization_map_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/visualization/map.md"
                            ),
                            mathjax=True,
                        ),
                        id="visualization_map_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="visualization_map_download_btn",
            ),
            dcc.Download(id="visualization_map_download"),
        ]
    )


@my_app.callback(
    Output("visualization_map_download", "data"),
    Input("visualization_map_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/visualization/map_code.py")


def map_info():
    return (map_content(), map_layout(), map_code())


@my_app.callback(
    Output("visualization_map_collapse", "is_open"),
    [Input("visualization_map_collapse_button", "n_clicks")],
    [State("visualization_map_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
