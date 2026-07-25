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

# perform the log transformation
prices = np.log1p(df_filtered["price"])

# calculate the quantiles for the QQ plot
quantiles = probplot(prices, dist="norm")

# extract the ordered values and the theoretical quantiles
ordered_values = quantiles[0][1]
theoretical_quantiles = quantiles[0][0]

# calculate the trend line (fit line) values
fit_values = quantiles[1][1] + quantiles[1][0] * theoretical_quantiles

# create the QQ plot figure
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=theoretical_quantiles, y=ordered_values, mode="markers", name="Quantiles"
    )
)
fig.add_trace(
    go.Scatter(x=theoretical_quantiles, y=fit_values, mode="lines", name="Fit")
)

fig.update_layout(
    title="QQ Plot of Log-transformed Prices",
    xaxis_title="Theoretical Quantiles",
    yaxis_title="Ordered Values",
)


def qq_plot_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def qq_plot_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The QQ plot of prices shows that the distribution of prices does not perfectly follow a normal distribution, as the points does not directly fit with the red line, especially at the lower and higher quantiles. This suggests that even after a log transformation (a non-linear transformation), there are extreme values in the data. Indeed that 'prices' does not follow the Gaussian (normal) distribution."
                    )
                ]
            ),
        ]
    )


def qq_plot_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_qq_plot_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/qq_plot.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_qq_plot_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_qq_plot_download_btn",
            ),
            dcc.Download(id="analysis_qq_plot_download"),
        ]
    )


@my_app.callback(
    Output("analysis_qq_plot_download", "data"),
    Input("analysis_qq_plot_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/qq_plot_code.py")


def qq_plot_info():
    return (qq_plot_content(), qq_plot_layout(), qq_plot_code())


@my_app.callback(
    Output("analysis_qq_plot_collapse", "is_open"),
    [Input("analysis_qq_plot_collapse_button", "n_clicks")],
    [State("analysis_qq_plot_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
