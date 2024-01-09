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

# create a violin plot
fig = px.violin(
    df_filtered,
    x="interest_level",
    y="price",
    color="interest_level",
    box=True,
    points="all",
)

fig.update_layout(
    title="Violin Plot of Interest Rate vs. Price",
    xaxis_title="Interest Level",
    yaxis_title="Price",
    title_x=0.5,
)


def violin_plot_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def violin_plot_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The violin plot shows the distribution of prices at different interest levels. It demonstratd that lower-priced listings have a wider range of prices and are more commonly found at the 'low' interest level, while the 'high' interest level has a narrower price distribution, indicating that high-interest listings are more consistently priced. The 'medium' interest level shows a price distribution that is somewhat between the 'low' and 'high' interest levels."
                    )
                ]
            ),
        ]
    )


def violin_plot_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_violin_plot_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/violin_plot.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_violin_plot_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_violin_plot_download_btn",
            ),
            dcc.Download(id="analysis_violin_plot_download"),
        ]
    )


@my_app.callback(
    Output("analysis_violin_plot_download", "data"),
    Input("analysis_violin_plot_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/violin_plot_code.py")


def violin_plot_info():
    return (violin_plot_content(), violin_plot_layout(), violin_plot_code())


@my_app.callback(
    Output("analysis_violin_plot_collapse", "is_open"),
    [Input("analysis_violin_plot_collapse_button", "n_clicks")],
    [State("analysis_violin_plot_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
