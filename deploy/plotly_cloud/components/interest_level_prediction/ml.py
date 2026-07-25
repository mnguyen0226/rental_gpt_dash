# dash imports
import dash
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import dash_bootstrap_components as dbc
from dash import State
import joblib
import pandas as pd

# file imports
from maindash import my_app
from utils.file_operation import read_file_as_str

# load trained model
models = {
    "Support Vector Machine": joblib.load("models/svm_model_generic_cls.pkl"),
    "Multi-layer Perceptron": joblib.load("models/mlp_model_generic_cls.pkl"),
    "Random Forest": joblib.load("models/rf_model_generic_cls.pkl"),
    "Decision Tree": joblib.load("models/dt_model_generic_cls.pkl"),
    "K-Nearest Neighbor": joblib.load("models/knn_model_generic_cls.pkl"),
}


def ml_content():
    layout = html.Div(
        [
            html.Div([html.H3("🧠 Select Model")]),
            dcc.Dropdown(
                id="ilp_ml_model_selector",
                options=[{"label": key, "value": key} for key in models.keys()],
                value="Decision Tree",
            ),
            html.Br(),
            html.Br(),
            dbc.Button(
                "Predict Interest Level",
                color="success",
                className="me-1",
                id="ilp_ml_predict_button",
                n_clicks=0,
            ),
            html.Br(),
            html.Br(),
            html.Div(
                [
                    dbc.Modal(
                        [
                            dbc.ModalHeader(dbc.ModalTitle("Prediction Result")),
                            dbc.ModalBody(html.Div(id="ilp_ml_prediction_output")),
                            dbc.ModalFooter(
                                dbc.Button(
                                    "Close",
                                    id="ilp_ml_close_modal",
                                    className="ml-auto",
                                )
                            ),
                        ],
                        id="ilp_ml_modal",
                        is_open=False,
                    ),
                ]
            ),
        ]
    )
    return layout


def ml_layout():
    return html.Div(
        [
            html.Div([html.H3("🏘️ Enter Apartment Preference")]),
            # slider for each feature
            html.Label("Number of Bathrooms", style={"fontWeight": "bold"}),
            dcc.Slider(
                id="ilp_ml_bathrooms_slider",
                min=0,
                max=10,
                step=0.5,
                value=2,
                marks=None,
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            html.Br(),
            html.Label("Number of Bedrooms", style={"fontWeight": "bold"}),
            dcc.Slider(
                id="ilp_ml_bedrooms_slider",
                min=0,
                max=8,
                step=0.5,
                value=5,
                marks=None,
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            html.Br(),
            html.Label("Estimated Price", style={"fontWeight": "bold"}),
            dcc.Slider(
                id="ilp_ml_price_slider",
                min=43,
                max=13000,
                step=100,
                value=2643,
                marks=None,
                tooltip={"placement": "bottom", "always_visible": True},
            ),
            html.Br(),
            html.Label(
                "Apartment's Description Evaluation", style={"fontWeight": "bold"}
            ),
            dcc.RadioItems(
                id="ilp_ml_description_slider",
                options=[
                    {"label": "Positive", "value": 1},
                    {"label": "Neutral", "value": 0},
                    {"label": "Negative", "value": -1},
                ],
                value=1,
                style={"margin": "auto"},
            ),
            html.Br(),
            html.Label("Has Laundry", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="ilp_ml_laundry_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Dishwasher", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="ilp_ml_dishwasher_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=0,
            ),
            html.Br(),
            html.Label("Has Hardwood Floors", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="ilp_ml_hardwood_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Allow Dog", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="ilp_ml_dog_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=0,
            ),
            html.Br(),
            html.Label("Allow Cat", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="ilp_ml_cat_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Doorman", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="ilp_ml_doorman_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Elevator", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="ilp_ml_elevator_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Application Fee", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="ilp_ml_fee_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Fitness Center", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="ilp_ml_fitness_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
        ]
    )


@my_app.callback(
    [Output("ilp_ml_modal", "is_open"), Output("ilp_ml_prediction_output", "children")],
    [
        Input("ilp_ml_predict_button", "n_clicks"),
        Input("ilp_ml_close_modal", "n_clicks"),
    ],
    [
        State("ilp_ml_modal", "is_open"),
        State("ilp_ml_model_selector", "value"),
        State("ilp_ml_bathrooms_slider", "value"),
        State("ilp_ml_bedrooms_slider", "value"),
        State("ilp_ml_price_slider", "value"),
        State("ilp_ml_description_slider", "value"),
        State("ilp_ml_laundry_slider", "value"),
        State("ilp_ml_dishwasher_slider", "value"),
        State("ilp_ml_hardwood_slider", "value"),
        State("ilp_ml_dog_slider", "value"),
        State("ilp_ml_cat_slider", "value"),
        State("ilp_ml_doorman_slider", "value"),
        State("ilp_ml_elevator_slider", "value"),
        State("ilp_ml_fee_slider", "value"),
        State("ilp_ml_fitness_slider", "value"),
    ],
)
def toggle_modal(
    n_clicks_predict,
    n_clicks_close,
    is_open,
    selected_model,
    bathrooms,
    bedrooms,
    price,
    description,
    laundry,
    dishwasher,
    hardwood,
    dog,
    cat,
    doorman,
    elevator,
    fee,
    fitness,
):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = "No clicks yet"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "ilp_ml_predict_button" and n_clicks_predict:
        cols = [
            "bathrooms",
            "bedrooms",
            "price",
            "sentiment_label",
            "feature_laundry in building",
            "feature_dishwasher",
            "feature_hardwood floors",
            "feature_dogs allowed",
            "feature_cats allowed",
            "feature_doorman",
            "feature_elevator",
            "feature_no fee",
            "feature_fitness center",
        ]
        input_data = pd.DataFrame(
            [
                [
                    bathrooms,
                    bedrooms,
                    price,
                    description,
                    laundry,
                    dishwasher,
                    hardwood,
                    dog,
                    cat,
                    doorman,
                    elevator,
                    fee,
                    fitness,
                ]
            ],
            columns=cols,
        )

        model = models[selected_model]
        prediction = model.predict(input_data)
        interest_level = {
            1: "High",
            0: "Medium",
            -1: "Low",
        }
        prediction_text = (
            f"Predicted Customer's Interest Level: {interest_level[prediction[0]]}"
        )
        return True, prediction_text

    elif button_id == "ilp_ml_close_modal" and n_clicks_close:
        return False, ""

    return is_open, ""


def ml_info():
    return (ml_content(), ml_layout())
