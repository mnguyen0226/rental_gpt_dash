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

# bar plot data preparation
bathroom_counts = df_filtered["bathrooms"].value_counts().sort_index()

# create a Plotly bar chart
fig = px.bar(
    x=bathroom_counts.index,
    y=bathroom_counts.values,
    labels={"x": "Number of Bathrooms", "y": "Number of Occurrence"},
)
fig.update_layout(
    title_text="Bar Chart of Number of Bathrooms Counts",
    title_x=0.5,
)


def bar_plot_2_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def bar_plot_2_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The bar chart indicates the number of bathrooms in listings shows that one-bathroom units are the most common, followed by two-bathroom units. Three or more bathrooms are relatively rare. This pattern suggests that the housing market in New York city primarily adjusts to singles and small families. Properties with a higher number of bathrooms are less common and could potentially offer to a luxury market segment."
                    )
                ]
            ),
        ]
    )


def bar_plot_2_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_bar_plot_2_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/bar_plot_2.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_bar_plot_2_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_bar_plot_2_download_btn",
            ),
            dcc.Download(id="analysis_bar_plot_2_download"),
        ]
    )


@my_app.callback(
    Output("analysis_bar_plot_2_download", "data"),
    Input("analysis_bar_plot_2_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/bar_plot_2_code.py")


def bar_plot_2_info():
    return (bar_plot_2_content(), bar_plot_2_layout(), bar_plot_2_code())


@my_app.callback(
    Output("analysis_bar_plot_2_collapse", "is_open"),
    [Input("analysis_bar_plot_2_collapse_button", "n_clicks")],
    [State("analysis_bar_plot_2_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
