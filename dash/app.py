# dash imports
import dash
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import dash_bootstrap_components as dbc

# file imports
from maindash import my_app

#######################################
# Initial Settings
#######################################
server = my_app.server

CONTENT_STYLE = {
    "transition": "margin-left .1s",
    "padding": "1rem 1rem",
}

#######################################
# Layout
########################################
sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("RentalGPT", style={"color": "white"}),
            ],
            className="sidebar-header",
        ),
        html.Br(),
        html.Div(style={"border-top": "2px solid white"}),
        html.Br(),
        # nav component
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-solid fa-star me-2"), html.Span("Overview")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-home me-2"),
                        html.Span("Apartment Listing"),
                    ],
                    href="/listing",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-chart-simple me-2"),
                        html.Span("Analysis"),
                    ],
                    href="/analysis",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-sliders me-2"),
                        html.Span("Visualization"),
                    ],
                    href="/visualization",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-people-group me-2"),
                        html.Span("Interest Level Prediction"),
                    ],
                    href="/interest_level_prediction",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-arrow-trend-up me-2"),
                        html.Span("Price Prediction"),
                    ],
                    href="/price_prediction",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-eye me-2"),
                        html.Span("Apartment Vision"),
                    ],
                    href="/apartment_vision",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-comments me-2"),
                        html.Span("Virtual Assistant"),
                    ],
                    href="/virtual_assistant",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-code me-2"),
                        html.Span("About"),
                    ],
                    href="/about",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)


my_app.layout = html.Div(
    [
        dcc.Location(id="url"),
        sidebar,
        html.Div(
            [
                dash.page_container,
            ],
            className="content",
            style=CONTENT_STYLE,  # Add the style here
            id="page-content",
        ),
    ]
)


@my_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        pass
    elif pathname == "/listing":
        pass
    elif pathname == "/analysis":
        pass
    elif pathname == "/visualization":
        pass
    elif pathname == "/interest_level_prediction":
        pass
    elif pathname == "/price_prediction":
        pass
    elif pathname == "/apartment_vision":
        pass
    elif pathname == "/virtual_assistant":
        pass
    elif pathname == "/about":
        pass
    return dbc.Container(
        children=[
            html.H1(
                "404 Error: Page Not found",
                style={"textAlign": "center", "color": "#082446"},
            ),
            html.Br(),
            html.P(
                f"Oh no! The pathname '{pathname}' was not recognised...",
                style={"textAlign": "center"},
            ),
            # image
            html.Div(
                style={"display": "flex", "justifyContent": "center"},
                children=[
                    html.Img(
                        src="https://elephant.art/wp-content/uploads/2020/02/gu_announcement_01-1.jpg",
                        alt="hokie",
                        style={"width": "400px"},
                    ),
                ],
            ),
        ]
    )


if __name__ == "__main__":
    my_app.run_server(debug=True, host="0.0.0.0", port=80)
