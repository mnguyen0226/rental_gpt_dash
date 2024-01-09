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

# sampling data for the 3D plot
sampled_df = df_filtered[["bedrooms", "bathrooms", "price"]].sample(n=1000)

# create a 3D scatter plot with Plotly Express
fig = px.scatter_3d(
    sampled_df,
    x="bedrooms",
    y="bathrooms",
    z="price",
    color="price",
    title="3D Plot of Price by Bedrooms and Bathrooms",
)

# update layout of the plot
fig.update_layout(
    title={"text": "3D Plot of Price by Bedrooms and Bathrooms", "x": 0.5},
    legend_title_text="Price",
)


def plot_3d_layout():
    layout = html.Div(
        [
            dcc.Loading(children=[dcc.Graph(figure=fig)]),
        ]
    )
    return layout


def plot_3d_content():
    return html.Div(
        [
            html.Div([html.H3("👁‍🗨 Observations")]),
            html.Div(
                [
                    html.P(
                        "The 3D scatter plot provides a visual representation of the relationship between the number of bedrooms and bathrooms against the price. It shows that generally, as the number of bedrooms and bathrooms increases, so does the price. The spread in the 'price' dimension suggests variability in pricing at similar bedroom and bathroom counts, which could be due to other (known/unknown) factors like location and apartment size."
                    )
                ]
            ),
        ]
    )


def plot_3d_code():
    return html.Div(
        [
            html.H3("💻 Source Code"),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "View Code",
                        id="analysis_plot_3d_collapse_button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dcc.Markdown(
                            children=read_file_as_str(
                                "./utils/markdown/analysis/plot_3d.md"
                            ),
                            mathjax=True,
                        ),
                        id="analysis_plot_3d_collapse",
                        is_open=False,
                    ),
                ]
            ),
            dbc.Button(
                "Download Code",
                color="success",
                className="me-1",
                id="analysis_plot_3d_download_btn",
            ),
            dcc.Download(id="analysis_plot_3d_download"),
        ]
    )


@my_app.callback(
    Output("analysis_plot_3d_download", "data"),
    Input("analysis_plot_3d_download_btn", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file("./utils/download_codes/analysis/plot_3d_code.py")


def plot_3d_info():
    return (plot_3d_content(), plot_3d_layout(), plot_3d_code())


@my_app.callback(
    Output("analysis_plot_3d_collapse", "is_open"),
    [Input("analysis_plot_3d_collapse_button", "n_clicks")],
    [State("analysis_plot_3d_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
