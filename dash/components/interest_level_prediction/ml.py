# dash imports
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
    "Support Vector Machine": joblib.load(
        "../notebooks/models/svm_model_generic_cls.pkl"
    ),
    "Multi-layer Perceptron": joblib.load(
        "../notebooks/models/mlp_model_generic_cls.pkl"
    ),
    "Random Forest": joblib.load("../notebooks/models/rf_model_generic_cls.pkl"),
    "Decision Tree": joblib.load("../notebooks/models/dt_model_generic_cls.pkl"),
    "K-Nearest Neighbor": joblib.load("../notebooks/models/knn_model_generic_cls.pkl"),
}

image_urls = {
    "High": "path_or_url_to_high_image.jpg",
    "Medium": "path_or_url_to_medium_image.jpg",
    "Low": "path_or_url_to_low_image.jpg",
}


def ml_content():
    layout = html.Div(
        [
            html.Div([html.H3("🧠 Select Model")]),
            dcc.Dropdown(
                id="model_selector",
                options=[{"label": key, "value": key} for key in models.keys()],
                value="Decision Tree",
            ),
            html.Br(),
            html.Br(),
            html.Div([html.H3("🏘️ Enter Apartment Preference")]),
            # slider for each feature
            html.Label("Number of Bathrooms", style={"fontWeight": "bold"}),
            dcc.Slider(
                id="bathrooms_slider",
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
                id="bedrooms_slider",
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
                id="price_slider",
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
                id="description_slider",
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
                id="laundry_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Dishwasher", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="dishwasher_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=0,
            ),
            html.Br(),
            html.Label("Has Hardwood Floors", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="hardwood_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Allow Dog", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="dog_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=0,
            ),
            html.Br(),
            html.Label("Allow Cat", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="cat_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Doorman", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="doorman_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Elevator", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="elevator_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Application Fee", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="fee_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            html.Label("Has Fitness Center", style={"fontWeight": "bold"}),
            dcc.RadioItems(
                id="fitness_slider",
                options=[
                    {"label": "Yes", "value": 1},
                    {"label": "No", "value": 0},
                ],
                value=1,
            ),
            html.Br(),
            dbc.Button(
                "Predict Interest Level",
                color="success",
                className="me-1",
                id="predict_button",
                n_clicks=0,
            ),
        ]
    )
    return layout


def ml_layout():
    return html.Div(
        [
            html.Div([html.H3("👇 Result")]),
            html.Div(
                [
                    html.Div(id="prediction_output"),
                ]
            ),
        ]
    )


@my_app.callback(
    Output("prediction_output", "children"),
    [Input("predict_button", "n_clicks")],
    [
        State("model_selector", "value"),
        State("bathrooms_slider", "value"),
        State("bedrooms_slider", "value"),
        State("price_slider", "value"),
        State("description_slider", "value"),
        State("laundry_slider", "value"),
        State("dishwasher_slider", "value"),
        State("hardwood_slider", "value"),
        State("dog_slider", "value"),
        State("cat_slider", "value"),
        State("doorman_slider", "value"),
        State("elevator_slider", "value"),
        State("fee_slider", "value"),
        State("fitness_slider", "value"),
    ],
)
def predict(
    n_clicks,
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
    if n_clicks > 0:
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
        interest_level = {1: "High", 0: "Medium", -1: "Low"}
        return f"Predicted Interest Level: {interest_level[prediction[0]]}"

    return ""


def ml_info():
    return (ml_content(), ml_layout())
