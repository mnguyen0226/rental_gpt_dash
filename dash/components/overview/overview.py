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
                                [
                                    dbc.CardImg(
                                        src="https://www.investopedia.com/thmb/bfHtdFUQrl7jJ_z-utfh8w1TMNA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/houses_and_land-5bfc3326c9e77c0051812eb3.jpg",
                                        top=True,
                                        style={
                                            "opacity": 0.18,
                                            "height": "200px",
                                        },
                                    ),
                                    dbc.CardImgOverlay(
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
                                                    href="",
                                                    className="mx-auto d-block",  # center the button horizontally
                                                ),
                                            ],
                                            className="text-center",  # center the card body content vertically
                                        ),
                                    ),
                                ],
                                style={"width": "18rem"},
                            ),
                            html.Br(),
                        ]
                    ),
                    html.Br(),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://cdn.thenewstack.io/media/2023/01/285d68dd-charts-1024x581.jpg",
                                        top=True,
                                        style={
                                            "opacity": 0.18,
                                            "height": "200px",
                                        },
                                    ),
                                    dbc.CardImgOverlay(
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
                                                # html.P(
                                                #     "An example of using an image in the background of "
                                                #     "a card.",
                                                #     className="card-text",
                                                # ),
                                                dbc.Button(
                                                    "Explore",
                                                    color="dark",
                                                    href="",
                                                    className="mx-auto d-block",  # center the button horizontally
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                style={"width": "18rem"},
                            ),
                            html.Br(),
                        ]
                    ),
                    html.Br(),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://media.licdn.com/dms/image/C4D12AQENxlEKXtt4Tw/article-cover_image-shrink_600_2000/0/1588295143025?e=2147483647&v=beta&t=3A_tBd2veQHzontm2NcuQ4lSuxL4lRNMeZJ8vw1MkOc",
                                        top=True,
                                        style={
                                            "opacity": 0.18,
                                            "height": "200px",
                                        },
                                    ),
                                    dbc.CardImgOverlay(
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
                                                # html.P(
                                                #     "An example of using an image in the background of "
                                                #     "a card.",
                                                #     className="card-text",
                                                # ),
                                                dbc.Button(
                                                    "Explore",
                                                    color="dark",
                                                    href="",
                                                    className="mx-auto d-block",  # center the button horizontally
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                style={"width": "18rem"},
                            ),
                            html.Br(),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://cdn.gobankingrates.com/wp-content/uploads/2023/06/house-for-sale-iStock-1470005312.jpg",
                                        top=True,
                                        style={
                                            "opacity": 0.18,
                                            "height": "200px",
                                        },
                                    ),
                                    dbc.CardImgOverlay(
                                        dbc.CardBody(
                                            [
                                                html.Div(
                                                    style={"height": "100px"},
                                                    children=[
                                                        html.H4(
                                                            "Interest Level Prediction",
                                                            className="card-title text-center",  # apply text-center class
                                                        ),
                                                    ],
                                                ),
                                                # html.P(
                                                #     "An example of using an image in the background of "
                                                #     "a card.",
                                                #     className="card-text",
                                                # ),
                                                dbc.Button(
                                                    "Explore",
                                                    color="dark",
                                                    href="",
                                                    className="mx-auto d-block",  # center the button horizontally
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
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
                                [
                                    dbc.CardImg(
                                        src="https://www.vantage-ai.com/hubfs/House%20prices.jpg",
                                        top=True,
                                        style={
                                            "opacity": 0.18,
                                            "height": "200px",
                                        },
                                    ),
                                    dbc.CardImgOverlay(
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
                                                # html.P(
                                                #     "An example of using an image in the background of "
                                                #     "a card.",
                                                #     className="card-text",
                                                # ),
                                                dbc.Button(
                                                    "Explore",
                                                    color="dark",
                                                    href="",
                                                    className="mx-auto d-block",  # center the button horizontally
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                style={"width": "18rem"},
                            ),
                            html.Br(),
                        ]
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src="https://huggingface.co/wordcab/llama-natural-instructions-7b/resolve/main/llama-natural-instructions-removebg-preview.png",
                                        top=True,
                                        style={
                                            "opacity": 0.18,
                                            "height": "200px",
                                        },
                                    ),
                                    dbc.CardImgOverlay(
                                        dbc.CardBody(
                                            [
                                                html.Div(
                                                    style={"height": "100px"},
                                                    children=[
                                                        html.H4(
                                                            "LlaMA Virtual Assistant",
                                                            className="card-title text-center",  # apply text-center class
                                                        ),
                                                    ],
                                                ),
                                                # html.P(
                                                #     "An example of using an image in the background of "
                                                #     "a card.",
                                                #     className="card-text",
                                                # ),
                                                dbc.Button(
                                                    "Explore",
                                                    color="dark",
                                                    href="",
                                                    className="mx-auto d-block",  # center the button horizontally
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                style={"width": "18rem"},
                            ),
                            html.Br(),
                        ]
                    ),
                ],
                className="mb-4",
            ),
        ],
    )
    return layout
