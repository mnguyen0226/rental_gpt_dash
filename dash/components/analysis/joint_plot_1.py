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
import plotly.graph_objs as go

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

# map the 'interest_level' to colors
interest_level_colors = {"low": "green", "medium": "orange", "high": "red"}
df_filtered["color"] = df_filtered["interest_level"].map(interest_level_colors)

# create a scatter plot
scatter_plot = go.Scatter(
    x=df_filtered["price"],
    y=df_filtered["bedrooms"],
    mode="markers",
    marker=dict(size=5, color=df_filtered["color"]),
    name="Scatter Plot",
)

# create a 2D histogram contour plot for the KDE
kde_plot = go.Histogram2dContour(
    x=df_filtered["price"],
    y=df_filtered["bedrooms"],
    colorscale="Blues",
    reversescale=True,
    xaxis="x",
    yaxis="y",
)

fig = go.Figure(data=[kde_plot, scatter_plot])

fig.update_layout(
    title="Joint Plot of Price vs. Number of Bedrooms",
    xaxis_title="Prices",
    yaxis_title="Number of Bedrooms",
    title_x=0.5,
)


def joint_plot_1_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def joint_plot_1_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The joint plot showcases the relationship between the price, the number of bedrooms, and the interest level of listings. The scatter points are color-coded by interest level, indicating that listings with high interest are not necessarily those with the highest price or most bedrooms. It suggests that while there might be a trend for higher prices with more bedrooms, the interest level is influenced by (known/unknown) factors beyond just these two."
                    )
                ]
            ),
        ]
    )


def joint_plot_1_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_joint_plot_1_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/joint_plot_1.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_joint_plot_1_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_joint_plot_1_download_btn",
            ),
            dcc.Download(id="analysis_joint_plot_1_download"),
        ]
    )


@my_app.callback(
    Output("analysis_joint_plot_1_download", "data"),
    Input("analysis_joint_plot_1_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/joint_plot_1_code.py")


def joint_plot_1_info():
    return (joint_plot_1_content(), joint_plot_1_layout(), joint_plot_1_code())


@my_app.callback(
    Output("analysis_joint_plot_1_collapse", "is_open"),
    [Input("analysis_joint_plot_1_collapse_button", "n_clicks")],
    [State("analysis_joint_plot_1_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
