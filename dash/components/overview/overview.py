# dash imports
import dash
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import dash_bootstrap_components as dbc

# file imports
from maindash import my_app
from utils.file_operation import read_file_as_str


#######################################
# Layout
#######################################
def overview_layout():
    layout = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="https://images.unsplash.com/photo-1614850523425-eec693b15af5?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                                style={
                                    "width": "100%",
                                    "height": "auto",
                                    "position": "relative",
                                },
                            ),
                        ],
                        style={
                            "height": "200px",
                            "overflow": "hidden",
                            "position": "relative",
                        },
                    ),
                    html.H1(
                        "App Overview",
                        style={
                            "position": "absolute",
                            "top": "80%",
                            "left": "50%",
                            "transform": "translate(-50%, -50%)",
                            "color": "white",
                            "text-align": "center",
                            "width": "100%",
                        },
                    ),
                ],
                style={
                    "position": "relative",
                    "text-align": "center",
                    "color": "white",
                },
            ),
            html.Br(),
            html.H3("🌟 Services"),
            dcc.Markdown(
                children=read_file_as_str("./utils/markdown/overview/overview.md"),
                mathjax=True,
            ),
            html.Br(),
            card(),
        ]
    )

    return layout


def card():
    layout = html.Div(
        html.Img(
            src="/assets/photos/RentalGPT_Won.png",
            style={
                "width": "100%",
                "maxWidth": "900px",
                "height": "auto",
                "display": "block",
                "margin-left": "auto",
                "margin-right": "auto",
            },
        ),
    )
    return layout
