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

# create distribution plot
fig = ff.create_distplot(
    [df_filtered["price"]], ["price"], show_hist=True, show_rug=True
)

# add vertical lines for mean and median
fig.add_vline(
    x=df_filtered["price"].mean(),
    line_dash="dash",
    line_color="red",
    annotation_text="Mean",
    annotation_position="top left",
)
fig.add_vline(
    x=df_filtered["price"].median(),
    line_dash="solid",
    line_color="green",
    annotation_text="Median",
    annotation_position="bottom right",
)

# update layout of the plot
fig.update_layout(
    title="Distribution Plot of Prices",
    xaxis_title="Price",
    yaxis_title="Density",
    title_x=0.5,
)


def dist_plot_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def dist_plot_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The distribution plot of rental prices, with a KDE overlay, indicates that the distribution of prices is right-skewed, meaning there are a number of higher-priced listings pulling the mean above the median. The median price is a better indicator of the central tendency for this dataset due to the skew. The skewness in the price distribution suggests that while most of the rentals are at a lower price point, there are enough premium-priced rentals to skew the average price higher."
                    )
                ]
            ),
        ]
    )


def dist_plot_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_dist_plot_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/dist_plot.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_dist_plot_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_dist_plot_download_btn",
            ),
            dcc.Download(id="analysis_dist_plot_download"),
        ]
    )


@my_app.callback(
    Output("analysis_dist_plot_download", "data"),
    Input("analysis_dist_plot_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/dist_plot_code.py")


def dist_plot_info():
    return (dist_plot_content(), dist_plot_layout(), dist_plot_code())


@my_app.callback(
    Output("analysis_dist_plot_collapse", "is_open"),
    [Input("analysis_dist_plot_collapse_button", "n_clicks")],
    [State("analysis_dist_plot_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
