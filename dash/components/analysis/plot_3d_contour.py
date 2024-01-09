# dash imports
import plotly.graph_objs as go
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from dash import State
from scipy.interpolate import griddata

# file imports
from maindash import my_app
from maindash import df
from utils.file_operation import read_file_as_str

# # import the dataset
# url = "https://raw.githubusercontent.com/mnguyen0226/two_sigma_property_listing/main/data/train.json"
# df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

x = df_filtered["bedrooms"]
y = df_filtered["bathrooms"]
z = df_filtered["price"]
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# interpolation
zi = griddata((x, y), z, (xi, yi), method="cubic")

# create a 3D contour plot
fig = go.Figure(data=[go.Surface(z=zi, x=xi, y=yi, colorscale="Viridis")])

fig.update_layout(
    title={"text": "3D Contour Plot of Price by Bedrooms and Bathrooms", "x": 0.5},
    scene=dict(xaxis_title="Bedrooms", yaxis_title="Bathrooms", zaxis_title="Price"),
)


def plot_3d_contour_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def plot_3d_contour_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The 3D contour plot presents a visual representation of the relationship between the number of bedrooms and bathrooms and the price of rental properties. Peaks in the contour suggest that listings with a higher number of bedrooms and bathrooms tend to have higher prices. This 3D view allows for ab understanding of how these variables interact. The steepness (higher prices) in areas with more bathrooms indicates that bathrooms may have a stronger influence on price in this dataset compared to bedrooms."
                    )
                ]
            ),
        ]
    )


def plot_3d_contour_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_plot_3d_contour_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/plot_3d_contour.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_plot_3d_contour_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_plot_3d_contour_download_btn",
            ),
            dcc.Download(id="analysis_plot_3d_contour_download"),
        ]
    )


@my_app.callback(
    Output("analysis_plot_3d_contour_download", "data"),
    Input("analysis_plot_3d_contour_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/plot_3d_contour_code.py")


def plot_3d_contour_info():
    return (plot_3d_contour_content(), plot_3d_contour_layout(), plot_3d_contour_code())


@my_app.callback(
    Output("analysis_plot_3d_contour_collapse", "is_open"),
    [Input("analysis_plot_3d_contour_collapse_button", "n_clicks")],
    [State("analysis_plot_3d_contour_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
