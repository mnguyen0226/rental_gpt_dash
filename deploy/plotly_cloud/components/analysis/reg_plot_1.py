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

# create a regression plot
fig = px.scatter(
    df_filtered,
    x="bathrooms",
    y="bedrooms",
    trendline="ols",
    title="Regression Plot with Scatter Representation",
)

fig.update_layout(
    xaxis_title="Bathrooms",
    yaxis_title="Bedrooms",
    title_x=0.5,
)


def reg_plot_1_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def reg_plot_1_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The regression plot with scatter representation shows a positive correlation between the number of bathrooms and bedrooms in rental listings. The trend line suggests that as the number of bathrooms increases, the number of bedrooms typically increases as well. Most data points cluster at the lower end of both axes, indicating that listings with fewer bedrooms and bathrooms are more common."
                    )
                ]
            ),
        ]
    )


def reg_plot_1_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_reg_plot_1_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/reg_plot_1.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_reg_plot_1_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_reg_plot_1_download_btn",
            ),
            dcc.Download(id="analysis_reg_plot_1_download"),
        ]
    )


@my_app.callback(
    Output("analysis_reg_plot_1_download", "data"),
    Input("analysis_reg_plot_1_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/reg_plot_1_code.py")


def reg_plot_1_info():
    return (reg_plot_1_content(), reg_plot_1_layout(), reg_plot_1_code())


@my_app.callback(
    Output("analysis_reg_plot_1_collapse", "is_open"),
    [Input("analysis_reg_plot_1_collapse_button", "n_clicks")],
    [State("analysis_reg_plot_1_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
