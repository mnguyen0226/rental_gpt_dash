# dash imports
import dash
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import dash_bootstrap_components as dbc

# file imports
from maindash import my_app
from components.price_prediction.ml import ml_info


#######################################
# Layout
#######################################
def price_prediction_layout():
    layout = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="https://images.unsplash.com/photo-1649393832219-0ad856a1e119?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
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
                        "Rental Cost Prediction",
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
                                id="price_prediction_selected_tab",
                                children=[
                                    dbc.Tab(
                                        label="Classical Models",
                                        tab_id="price_prediction_ml",
                                    ),
                                    dbc.Tab(
                                        label="Classical Models - Images",
                                        tab_id="price_prediction_ml_img",
                                    ),
                                ],
                                active_tab="price_prediction_ml",
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
                            "width": "50%",
                            "padding": "10px",
                        },
                        children=[
                            html.Div(id="price_prediction_tab_content_layout"),
                        ],
                    ),
                    html.Div(
                        style={
                            "width": "50%",
                            "padding": "10px",
                        },
                        children=[
                            html.Div(id="price_prediction_tab_plot_layout"),
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
            component_id="price_prediction_tab_content_layout",
            component_property="children",
        ),
        Output(
            component_id="price_prediction_tab_plot_layout",
            component_property="children",
        ),
    ],
    [
        Input(
            component_id="price_prediction_selected_tab",
            component_property="active_tab",
        )
    ],
)
def render_tab(tab_choice):
    """Renders the selected subtab's layout

    Args:
        tab_choice (str): selected subtab

    Returns:
        selected subtab's layout
    """
    if tab_choice == "price_prediction_ml":
        return ml_info()
    if tab_choice == "price_prediction_ml_img":
        note = (
            html.Div(
                [
                    html.Div([html.H3("🧪 Experimentation")]),
                    html.P(
                        [
                            "Due to the lack of data and poor performance of the trained model, I have decided not to deploy this tab. General idea: The user will be able to attach image(s), YOLOv5 will extract additional features of interests, which will (hopefully) help the ML make a more accurate prediction. The code of this prototype can be accessed ",
                            html.A(
                                "here",
                                href="https://github.com/mnguyen0226/two_sigma_property_listing/tree/main/experimentation/price_prediction_with_images",
                                target="_blank",
                            ),
                            ".",
                        ]
                    ),
                ]
            ),
        )
        return note, ""
