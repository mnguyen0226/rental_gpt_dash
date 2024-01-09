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
import plotly.figure_factory as ff

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

fig = ff.create_scatterplotmatrix(
    df_filtered[["bathrooms", "bedrooms", "price"]],
    diag="histogram",
    height=800,
    width=800,
)
axis_titles = ["bathrooms", "bedrooms", "price"]
for i, axis_title in enumerate(axis_titles, start=1):
    fig["layout"]["xaxis{}".format(i)].update(title=axis_title)
    fig["layout"]["yaxis{}".format(i)].update(title=axis_title)

fig["layout"]["xaxis4"]["title"] = "bathrooms"
fig["layout"]["xaxis5"]["title"] = "bedrooms"
fig["layout"]["xaxis6"]["title"] = "price"

fig.update_layout(
    title="Feature Pair Plot",
    title_x=0.5,
    showlegend=False,
)


def pair_plot_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def pair_plot_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The pair plot indicates relationships between the number of bathrooms, bedrooms, and price. There is a positive correlation between the number of bathrooms and bedrooms, which is intuitive as larger homes tend to have more of both. The scatter plots also suggest a positive correlation between price and both the number of bedrooms and bathrooms, indicating that as the count of these features increases, so does the price."
                    )
                ]
            ),
        ]
    )


def pair_plot_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_pair_plot_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/pair_plot.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_pair_plot_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_pair_plot_download_btn",
            ),
            dcc.Download(id="analysis_pair_plot_download"),
        ]
    )


@my_app.callback(
    Output("analysis_pair_plot_download", "data"),
    Input("analysis_pair_plot_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/pair_plot_code.py")


def pair_plot_info():
    return (pair_plot_content(), pair_plot_layout(), pair_plot_code())


@my_app.callback(
    Output("analysis_pair_plot_collapse", "is_open"),
    [Input("analysis_pair_plot_collapse_button", "n_clicks")],
    [State("analysis_pair_plot_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
