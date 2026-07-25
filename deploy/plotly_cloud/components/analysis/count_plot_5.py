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
df_filtered["weekday"] = pd.to_datetime(df_filtered["created"]).dt.weekday
count_df = (
    df_filtered.groupby(["weekday", "interest_level"]).size().reset_index(name="count")
)

# create the bar plot using the count data
fig = px.bar(
    count_df,
    x="weekday",
    y="count",
    color="interest_level",
    category_orders={"interest_level": ["low", "medium", "high"]},
    title="Bar Chart of Interest Level in Weekday",
    labels={"count": "Interest Level Counts"},
)

fig.update_layout(
    xaxis_title="Weekday",
    yaxis_title="Count",
    title_x=0.5,
    legend_title_text="Interest Level",
    barmode="group",
)


def count_plot_5_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def count_plot_5_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The bar chart shows the interest level counts across weekdays. It shows the lowest levels of interest typically on the first day of the week and higher interest levels in the middle of the week. The trend suggests that renters might be more actively looking for listings during mid-week rather than at the beginning or end of the week."
                    )
                ]
            ),
        ]
    )


def count_plot_5_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_count_plot_5_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/count_plot_5.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_count_plot_5_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_count_plot_5_download_btn",
            ),
            dcc.Download(id="analysis_count_plot_5_download"),
        ]
    )


@my_app.callback(
    Output("analysis_count_plot_5_download", "data"),
    Input("analysis_count_plot_5_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/count_plot_5_code.py")


def count_plot_5_info():
    return (count_plot_5_content(), count_plot_5_layout(), count_plot_5_code())


@my_app.callback(
    Output("analysis_count_plot_5_collapse", "is_open"),
    [Input("analysis_count_plot_5_collapse_button", "n_clicks")],
    [State("analysis_count_plot_5_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
