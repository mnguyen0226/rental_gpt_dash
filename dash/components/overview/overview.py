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
        # style={"width":"100px"},
        children=[
            dbc.Row(
                style={"display": "flex", "justifyContent": "flex-end"},
                children=[
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            style={"height": "100px"},
                                            children=[
                                                html.H4(
                                                    "New York City Apartments Listing",
                                                    className="card-title text-center",  # apply text-center class
                                                ),
                                            ],
                                        ),
                                        dbc.Button(
                                            "Explore",
                                            color="dark",
                                            href="https://rentalgpt.discovery.cs.vt.edu/listing",
                                            className="mx-auto d-block",  # center the button horizontally
                                        ),
                                    ],
                                    className="text-center",  # center the card body content vertically
                                ),
                                style={"width": "18rem"},
                            ),
                            html.Br(),
                        ]
                    ),
                    html.Br(),
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            style={"height": "100px"},
                                            children=[
                                                html.H4(
                                                    "In-depth Data Analysis",
                                                    className="card-title text-center",  # apply text-center class
                                                ),
                                            ],
                                        ),
                                        dbc.Button(
                                            "Explore",
                                            color="dark",
                                            href="https://rentalgpt.discovery.cs.vt.edu/analysis",
                                            className="mx-auto d-block",  # center the button horizontally
                                        ),
                                    ],
                                    className="text-center",
                                ),
                                style={"width": "18rem"},
                            ),
                            html.Br(),
                        ]
                    ),
                    html.Br(),
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            style={"height": "100px"},
                                            children=[
                                                html.H4(
                                                    "Interactive Data Visualization",
                                                    className="card-title text-center",  # apply text-center class
                                                ),
                                            ],
                                        ),
                                        dbc.Button(
                                            "Explore",
                                            color="dark",
                                            href="https://rentalgpt.discovery.cs.vt.edu/visualization",
                                            className="mx-auto d-block",  # center the button horizontally
                                        ),
                                    ],
                                    className="text-center",
                                ),
                                style={"width": "18rem"},
                            ),
                            html.Br(),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            style={"height": "100px"},
                                            children=[
                                                html.H4(
                                                    "Customer's Interest Level Prediction",
                                                    className="card-title text-center",  # apply text-center class
                                                ),
                                            ],
                                        ),
                                        dbc.Button(
                                            "Explore",
                                            color="dark",
                                            href="https://rentalgpt.discovery.cs.vt.edu/interest_level_prediction",
                                            className="mx-auto d-block",  # center the button horizontally
                                        ),
                                    ],
                                    className="text-center",
                                ),
                                style={"width": "18rem"},
                            ),
                        ]
                    ),
                    #     ],
                    #     className="mb-4",
                    # ),
                    # dbc.Row(
                    #     [
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            style={"height": "100px"},
                                            children=[
                                                html.H4(
                                                    "Monthly Rental Price Prediction",
                                                    className="card-title text-center",  # apply text-center class
                                                ),
                                            ],
                                        ),
                                        dbc.Button(
                                            "Explore",
                                            color="dark",
                                            href="https://rentalgpt.discovery.cs.vt.edu/price_prediction",
                                            className="mx-auto d-block",  # center the button horizontally
                                        ),
                                    ],
                                    className="text-center",
                                ),
                                style={"width": "18rem"},
                            ),
                            html.Br(),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            style={"height": "100px"},
                                            children=[
                                                html.H4(
                                                    "LLaMA Virtual Assistant",
                                                    className="card-title text-center",  # apply text-center class
                                                ),
                                            ],
                                        ),
                                        dbc.Button(
                                            "Explore",
                                            color="dark",
                                            href="https://rentalgpt.discovery.cs.vt.edu/virtual_assistant",
                                            className="mx-auto d-block",  # center the button horizontally
                                        ),
                                    ],
                                    className="text-center",
                                ),
                                style={"width": "18rem"},
                            ),
                        ]
                    ),
                ],
                className="mb-4",
            ),
            # html.Br(),
            # html.Hr(),
            # html.H3("📱Mobile App"),
        ],
    )
    return layout
