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

# get feature correlation
corr = df_filtered[["bathrooms", "bedrooms", "price"]].corr()

# create a heatmap with Plotly
fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    labels=dict(color="Correlation"),
    x=["bathrooms", "bedrooms", "price"],
    y=["bathrooms", "bedrooms", "price"],
)

fig.update_layout(
    title="Correlation Heatmap",
    title_x=0.5,
)


def heatmap_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def heatmap_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The heatmap displays the correlation matrix for bathrooms, bedrooms, and price. The values, ranging from 0.52 to 0.67, indicate a moderate positive correlation between these features. This means as the number of bedrooms or bathrooms increases, the price tends to increase as well. There is a strongest correlation between price and the number of bathrooms, suggesting that the number of bathrooms is a more significant factor in determining the price than the number of bedrooms."
                    )
                ]
            ),
        ]
    )


def heatmap_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_heatmap_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/heatmap.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_heatmap_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_heatmap_download_btn",
            ),
            dcc.Download(id="analysis_heatmap_download"),
        ]
    )


@my_app.callback(
    Output("analysis_heatmap_download", "data"),
    Input("analysis_heatmap_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/heatmap_code.py")


def heatmap_info():
    return (heatmap_content(), heatmap_layout(), heatmap_code())


@my_app.callback(
    Output("analysis_heatmap_collapse", "is_open"),
    [Input("analysis_heatmap_collapse_button", "n_clicks")],
    [State("analysis_heatmap_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
