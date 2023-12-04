# dash imports
import dash
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import dash_bootstrap_components as dbc

# file imports
from maindash import my_app
from components.virtual_assistant.chatbot import chatbot_info


#######################################
# Layout
#######################################
def virtual_assistant_layout():
    layout = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="https://images.unsplash.com/photo-1641160923894-b1a80920187d?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
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
                        "Virtual Assistant",
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
            html.Div(
                style={"display": "flex"},
                children=[
                    # tab
                    html.Div(
                        [
                            dbc.Tabs(
                                id="virtual_assistant_selected_tab",
                                children=[
                                    dbc.Tab(
                                        label="Llama Chatbot",
                                        tab_id="hugging_face",
                                    ),
                                    dbc.Tab(
                                        label="Alternative Solution",
                                        tab_id="streamlit",
                                    ),
                                ],
                                active_tab="hugging_face",
                            ),
                        ]
                    ),
                ],
            ),
            html.Br(),
            html.Br(),
            # content
            html.Div(
                style={"display": "flex"},
                children=[
                    html.Div(
                        style={
                            "width": "50%",
                            "padding": "10px",
                        },
                        children=[
                            html.Div(id="virtual_assistant_tab_content_layout"),
                        ],
                    ),
                    html.Div(
                        style={
                            "width": "50%",
                            # "height": "calc(70vh - 250px)",
                            # "overflow-y": "auto",
                            "padding": "10px",
                        },
                        children=[
                            html.Div(id="virtual_assistant_tab_plot_layout"),
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
        Output(
            component_id="virtual_assistant_tab_content_layout",
            component_property="children",
        ),
        Output(
            component_id="virtual_assistant_tab_plot_layout",
            component_property="children",
        ),
    ],
    [
        Input(
            component_id="virtual_assistant_selected_tab",
            component_property="active_tab",
        )
    ],
)
def render_tab_1(tab_choice):
    """Renders the selected subtab's layout

    Args:
        tab_choice (str): selected subtab

    Returns:
        selected subtab's layout
    """
    if tab_choice == "hugging_face":
        return chatbot_info()
    if tab_choice == "streamlit":
        return (
            html.P(
                "Note about streamlit. Remember to add code for simple llama template"
            ),
            html.P("images"),
        )
