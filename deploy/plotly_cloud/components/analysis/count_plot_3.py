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

# prepare the data for the plot
df_filtered["month"] = pd.to_datetime(df_filtered["created"]).dt.month
count_df = (
    df_filtered.groupby(["month", "interest_level"]).size().reset_index(name="count")
)

# create the bar plot using the count data
fig = px.bar(
    count_df,
    x="month",
    y="count",
    color="interest_level",
    category_orders={"interest_level": ["low", "medium", "high"]},
    title="Bar Chart of Interest Level in Month",
    labels={"count": "Interest Level Counts"},
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Count",
    title_x=0.5,
    legend_title_text="Interest Level",
    barmode="group",
)


def count_plot_3_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def count_plot_3_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The bar chart compares the interest level counts across three months, showing a clear summer seasonal trend. Interest levels, both low and medium, are highest in June and lower in the preceding months. The high interest levels do not show a significant monthly variation, suggesting that high interest properties are consistently sought after, regardless of the season. This trend is common in real estate markets due to various factors such as the end of the school year and the peak moving season (internship, co-op,...)."
                    )
                ]
            ),
        ]
    )


def count_plot_3_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_count_plot_3_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/count_plot_3.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_count_plot_3_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_count_plot_3_download_btn",
            ),
            dcc.Download(id="analysis_count_plot_3_download"),
        ]
    )


@my_app.callback(
    Output("analysis_count_plot_3_download", "data"),
    Input("analysis_count_plot_3_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/count_plot_3_code.py")


def count_plot_3_info():
    return (count_plot_3_content(), count_plot_3_layout(), count_plot_3_code())


@my_app.callback(
    Output("analysis_count_plot_3_collapse", "is_open"),
    [Input("analysis_count_plot_3_collapse_button", "n_clicks")],
    [State("analysis_count_plot_3_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
