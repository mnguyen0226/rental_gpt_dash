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

# create pie chart
fig = px.pie(df, names="interest_level", title="Percentages of Interests", hole=0.3)

fig.update_layout(
    title_x=0.5,
    legend_title_text="Interest Level",
)

fig.update_traces(textinfo="percent+label", pull=[0.1, 0, 0])


def pie_chart_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def pie_chart_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The pie chart presents the distribution of interest levels across rental listings. A large majority of the listings have a low interest level, while a smaller fraction have medium interest, and only a very small percentage show high interest. This distribution could be due to various factors like price, location, features, or listing quality. The low percentage of high interest listings may indicate a competitive market where only a few listings stand out enough to attract a high volume of potential renters in New York city."
                    )
                ]
            ),
        ]
    )


def pie_chart_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_pie_chart_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/pie_chart.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_pie_chart_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_pie_chart_download_btn",
            ),
            dcc.Download(id="analysis_pie_chart_download"),
        ]
    )


@my_app.callback(
    Output("analysis_pie_chart_download", "data"),
    Input("analysis_pie_chart_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/pie_chart_code.py")


def pie_chart_info():
    return (pie_chart_content(), pie_chart_layout(), pie_chart_code())


@my_app.callback(
    Output("analysis_pie_chart_collapse", "is_open"),
    [Input("analysis_pie_chart_collapse_button", "n_clicks")],
    [State("analysis_pie_chart_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
