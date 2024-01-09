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
def about_layout():
    layout = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="https://images.unsplash.com/photo-1614854262340-ab1ca7d079c7?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
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
                        "About",
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
            html.Div(
                style={"display": "flex"},
                children=[
                    dcc.Markdown(
                        children=read_file_as_str("./utils/markdown/about/about.md"),
                        mathjax=True,
                    ),
                ],
            ),
            card(),
            html.Br(),
            html.Hr(),
            html.H3(
                "Data Science Life Cycle",
                style={"textAlign": "center", "color": "#082446"},
            ),
            html.Br(),
            html.Img(
                src="https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/data_science_life_cycle.png",
                style={
                    "width": "1200px",
                    "display": "block",
                    "margin-left": "auto",
                    "margin-right": "auto",
                },
            ),
            html.Br(),
            html.Hr(),
            html.H3(
                "Architecture Design",
                style={"textAlign": "center", "color": "#082446"},
            ),
            html.Br(),
            html.Img(
                src="https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/rental_gpt_dash_architecture.png",
                style={
                    "width": "800px",
                    "display": "block",
                    "margin-left": "auto",
                    "margin-right": "auto",
                },
            ),
        ]
    )

    return layout


def card():
    layout = html.Div(
        [
            html.Br(),
            dbc.Card(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.CardImg(
                                    src="https://raw.githubusercontent.com/mnguyen0226/mnguyen0226.github.io/main/static/profile_images/personal/professional.png",
                                    className="img-fluid rounded-start",
                                ),
                                className="col-md-5",
                            ),
                            dbc.Col(
                                dbc.CardBody(
                                    children=[
                                        html.H4(
                                            "Minh T. Nguyen",
                                            className="card-title",
                                        ),
                                        html.P(
                                            "Research Assistant, "
                                            "M.Sc. Computer Engineering "
                                            "at Virginia Tech.",
                                            className="card-text",
                                        ),
                                        html.Small(
                                            "mnguyen0226@vt.edu",
                                            className="card-text text-muted",
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.A(
                                            html.Img(
                                                src="https://cdn-icons-png.flaticon.com/512/174/174857.png",
                                                alt="LinkedIn",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                    "marginRight": "10px",
                                                },
                                            ),
                                            href="https://www.linkedin.com/in/minhbtnguyen/",
                                            target="_blank",
                                            className="text-dark",
                                        ),
                                        html.A(
                                            html.Img(
                                                src="https://cdn-icons-png.flaticon.com/512/25/25231.png",
                                                alt="LinkedIn",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                },
                                            ),
                                            href="https://github.com/mnguyen0226",
                                            target="_blank",
                                            className="text-dark",
                                        ),
                                    ]
                                ),
                                className="col-md-7",
                            ),
                        ],
                        className="g-0 d-flex align-items-center",
                    )
                ],
                className="mb-3",
                style={"maxWidth": "540px"},
            ),
        ]
    )
    return layout
