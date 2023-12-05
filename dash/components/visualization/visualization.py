# dash imports
import dash
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import dash_bootstrap_components as dbc

# file imports
from maindash import my_app
from components.visualization.map import map_info
from components.visualization.price import price_info


#######################################
# Layout
#######################################
def visualization_layout():
    layout = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="https://images.unsplash.com/photo-1557683316-973673baf926?q=80&w=1129&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
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
                        "Data Visualization",
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
                    # tab
                    html.Div(
                        [
                            dbc.Tabs(
                                id="visualization_selected_tab",
                                children=[
                                    dbc.Tab(
                                        label="NYC Rental Map",
                                        tab_id="visualization_map",
                                    ),
                                    dbc.Tab(
                                        label="NYC Rental Price",
                                        tab_id="visualization_price",
                                    ),
                                ],
                                active_tab="visualization_map",
                            ),
                        ]
                    ),
                ],
            ),
            html.Br(),
            # content
            html.Div(
                style={"display": "flex"},
                children=[
                    html.Div(
                        style={
                            "width": "30%",
                            "padding": "10px",
                        },
                        children=[
                            html.Div(id="visualization_tab_content_layout"),
                        ],
                    ),
                    html.Div(
                        style={
                            "width": "70%",
                            "padding": "10px",
                        },
                        children=[
                            html.Div(id="visualization_tab_plot_layout"),
                        ],
                    ),
                ],
            ),
            html.Br(),
            html.Br(),
            # download and view code
            html.Div(id="visualization_code"),
        ]
    )

    return layout


#######################################
# Callbacks
#######################################
@my_app.callback(
    [
        Output(
            component_id="visualization_tab_content_layout",
            component_property="children",
        ),
        Output(
            component_id="visualization_tab_plot_layout", component_property="children"
        ),
        Output(component_id="visualization_code", component_property="children"),
    ],
    [Input(component_id="visualization_selected_tab", component_property="active_tab")],
)
def render_tab(tab_choice):
    """Renders the selected subtab's layout

    Args:
        tab_choice (str): selected subtab

    Returns:
        selected subtab's layout
    """
    if tab_choice == "visualization_map":
        return map_info()
    if tab_choice == "visualization_price":
        return price_info()
