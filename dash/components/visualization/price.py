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
from utils.file_operation import read_file_as_str

# import the dataset
url = "https://raw.githubusercontent.com/mnguyen0226/two_sigma_property_listing/main/data/train.json"
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]


def price_layout():
    layout = html.Div(
        [
            dcc.Loading(
                children=[dcc.Graph(id="visualization_price_line_plot")], type="circle"
            ),
        ]
    )
    return layout


def price_content():
    return html.Div(
        [
            html.Div([html.H3("🎛 Tune")]),
            html.Div(
                [
                    dcc.Dropdown(
                        id="visualization_price_dropdown",
                        options=[
                            {"label": "High Interest", "value": "high"},
                            {"label": "Medium Interest", "value": "medium"},
                            {"label": "Low Interest", "value": "low"},
                        ],
                        value="high",
                    ),
                ]
            ),
        ]
    )


# Callback to update line_plot based on dropdown selection
@my_app.callback(
    Output("visualization_price_line_plot", "figure"),
    [Input("visualization_price_dropdown", "value")],
)
def update_line_plot(selected_interest):
    df_filtered["date"] = pd.to_datetime(df_filtered["created"]).dt.date
    filtered_data = df_filtered[df_filtered["interest_level"] == selected_interest]
    df_grouped = filtered_data.groupby("date")["price"].mean().reset_index()

    fig = px.line(
        df_grouped,
        x="date",
        y="price",
        title=f"Average Property Prices Over Time - {selected_interest.capitalize()} Interest",
    )
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Average Price")
    fig.update_layout(title_x=0.5)

    return fig


def price_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="visualization_price_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/visualization/price.md"
                            ),
                            mathjax=True,
                        ),
                        id="visualization_price_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="visualization_price_download_btn",
            ),
            dcc.Download(id="visualization_price_download"),
        ]
    )


@my_app.callback(
    Output("visualization_price_download", "data"),
    Input("visualization_price_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/visualization/price_code.py")


def price_info():
    return (price_content(), price_layout(), price_code())


@my_app.callback(
    Output("visualization_price_collapse", "is_open"),
    [Input("visualization_price_collapse_button", "n_clicks")],
    [State("visualization_price_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
