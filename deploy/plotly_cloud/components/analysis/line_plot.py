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

# # read the data
# url = "https://raw.githubusercontent.com/mnguyen0226/two_sigma_property_listing/main/data/train.json"
# df = pd.read_json(url)


def line_plot_layout():
    layout = html.Div(
        [
            dcc.Loading(
                children=[
                    dcc.DatePickerRange(
                        id="analysis_line_plot_date",
                        start_date=pd.to_datetime("2016-04-01"),
                        end_date=pd.to_datetime("2016-07-01"),
                        display_format="YYYY-MM-DD",
                    ),
                    dcc.Graph(id="analysis_line_price_graph"),
                ],
            )
        ]
    )
    return layout


@my_app.callback(
    Output("analysis_line_price_graph", "figure"),
    [
        Input("analysis_line_plot_date", "start_date"),
        Input("analysis_line_plot_date", "end_date"),
    ],
)
def update_graph(start_date, end_date):
    # convert the date strings to datetime objects
    start_date = pd.to_datetime(start_date).date()
    end_date = pd.to_datetime(end_date).date()

    # outlier removal
    upper_bound = np.percentile(df["price"].values, 99)
    df_filtered = df[df["price"] <= upper_bound]

    # create new date columns
    df_filtered["date"] = pd.to_datetime(df_filtered["created"]).dt.date

    # filter data based on date range
    df_filtered = df_filtered[
        (df_filtered["date"] >= start_date) & (df_filtered["date"] <= end_date)
    ]

    # group by date and take the average of the price
    df_grouped = df_filtered.groupby("date")["price"].mean().reset_index()

    fig = px.line(
        df_grouped, x="date", y="price", title="Average Property Prices Over Time"
    )
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Average Price")
    fig.update_layout(title_x=0.5)

    return fig


def line_plot_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The line plot shows the price trend over time suggesting that rental prices fluctuate but do not exhibit a clear long-term trend in the given timeframe, which is sensible as our dataset is only 3-month long. There are spikes in rental prices that could correspond to specific events or seasonal demand changes. However, since we don't have an entire year-dataset, it's hard to determine the seasonality of the price trends for New York city apartments."
                    )
                ]
            ),
        ]
    )


def line_plot_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_line_plot_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/line_plot.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_line_plot_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_line_plot_download_btn",
            ),
            dcc.Download(id="analysis_line_plot_download"),
        ]
    )


@my_app.callback(
    Output("analysis_line_plot_download", "data"),
    Input("analysis_line_plot_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/line_plot_code.py")


def line_plot_info():
    return (line_plot_content(), line_plot_layout(), line_plot_code())


@my_app.callback(
    Output("analysis_line_plot_collapse", "is_open"),
    [Input("analysis_line_plot_collapse_button", "n_clicks")],
    [State("analysis_line_plot_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
