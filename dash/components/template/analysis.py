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
# Layout
#######################################
def analysis_layout():
    layout = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="https://images.unsplash.com/photo-1534477675274-cd511de4be22?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                                style={
                                    "width": "100%",
                                    "height": "auto",
                                    "position": "relative",
                                },
                            ),
                        ],
                        style={
                            "height": "300px",
                            "overflow": "hidden",
                            "position": "relative",
                        },
                    ),
                    html.H1(
                        "RentGPT",
                        style={
                            "position": "absolute",
                            "top": "80%",
                            "left": "50%",
                            "transform": "translate(-45%, -50%)",
                            "color": "white",
                            "text-align": "left",
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
            html.Div(
                style={"display": "flex"},
                children=[
                    # tab
                    html.Div(
                        [
                            dbc.Tabs(
                                id="selected_tab",
                                children=[
                                    dbc.Tab(
                                        label="Line Plot",
                                        tab_id="theory_tab",
                                    ),
                                    # here
                                ],
                                active_tab="theory_tab",
                            ),
                        ]
                    ),
                ],
            ),
            # content
            html.Div(
                style={"display": "flex"},
                children=[
                    html.Div(
                        style={
                            "width": "50%",
                            "padding": "20px",
                        },
                        children=[
                            html.Div(id="tab_content_layout"),
                        ],
                    ),
                    html.Div(
                        style={
                            "width": "50%",
                            "padding": "20px",
                        },
                        children=[
                            html.Div(id="tab_plot_layout"),
                        ],
                    ),
                ],
            ),
        ]
    )

    return layout


#######################################
# Callbacks
#######################################
@my_app.callback(
    [
        Output(component_id="tab_content_layout", component_property="children"),
        Output(component_id="tab_plot_layout", component_property="children"),
    ],
    [Input(component_id="selected_tab", component_property="active_tab")],
)
def render_tab_1(tab_choice):
    """Renders the selected subtab's layout

    Args:
        tab_choice (str): selected subtab

    Returns:
        selected subtab's layout
    """
    if tab_choice == "theory_tab":
        return (html.P("theory_tab"), html.P("theory_tab"))
    if tab_choice == "pg_tab":
        return (html.P("pg_tab"), html.P("pg_tab"))
    if tab_choice == "code_tab":
        return (html.P("code_tab"), html.P("code_tab"))
