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
from maindash import df
from utils.file_operation import read_file_as_str

# # import the dataset
# url = "https://raw.githubusercontent.com/mnguyen0226/two_sigma_property_listing/main/data/train.json"
# df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

# create the 'date' column to datetime
df_filtered["date"] = pd.to_datetime(df_filtered["created"]).dt.date

grouped = df_filtered.groupby(["date", "interest_level"])["price"].mean().reset_index()
pivot_df = grouped.pivot(index="date", columns="interest_level", values="price")

fig = go.Figure()

for interest_level in pivot_df.columns:
    fig.add_trace(
        go.Scatter(
            x=pivot_df.index,
            y=pivot_df[interest_level],
            fill="tozeroy",
            name=interest_level,
        )
    )

fig.update_layout(
    title="Area Plot of Prices Over Time by Interest Level",
    xaxis_title="Date",
    yaxis_title="Average Price",
    xaxis={"type": "date"},
    title_x=0.5,
)


def area_plot_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def area_plot_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The area plot reveals fluctuations in average listing prices over time across different interest levels. High interest properties generally command higher prices, while low interest properties are clustered at lower price points. The data indicates variability in the rental market, with occasional peaks suggesting the entry of premium listings or seasonal demand surges. The overlap between medium and high interest levels points to price being one of several factors influencing interest. Without having to analyse the annual dataset, it's hard to determine seasonality of low, medium, and high interest level."
                    )
                ]
            ),
        ]
    )


def area_plot_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_area_plot_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/area_plot.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_area_plot_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_area_plot_download_btn",
            ),
            dcc.Download(id="analysis_area_plot_download"),
        ]
    )


@my_app.callback(
    Output("analysis_area_plot_download", "data"),
    Input("analysis_area_plot_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/area_plot_code.py")


def area_plot_info():
    return (area_plot_content(), area_plot_layout(), area_plot_code())


@my_app.callback(
    Output("analysis_area_plot_collapse", "is_open"),
    [Input("analysis_area_plot_collapse_button", "n_clicks")],
    [State("analysis_area_plot_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
