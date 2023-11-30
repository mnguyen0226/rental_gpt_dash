import pandas as pd
from dash import Dash, html, dcc, Input, Output
from dash import State
import joblib
import dash_bootstrap_components as dbc
import torch
import base64
from io import BytesIO
from PIL import Image

# load YOLOv5 model
yolo_model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

interested_features = [
    "chair_count",
    "sink_count",
    "oven_count",
    "refrigerator_count",
    "toilet_count",
    "person_count",
    "potted plant_count",
    "microwave_count",
    "bottle_count",
    "tv_count",
]


def process_image(contents, interested_features):
    # convert base64 string to bytes
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)
    img = Image.open(BytesIO(decoded))

    # YOLOv5 feature extraction
    results = yolo_model(img)
    counts = results.pandas().xyxy[0]["name"].value_counts().to_dict()

    # count features of interest
    feature_data = {feature: 0 for feature in interested_features}
    for item, count in counts.items():
        feature_name = f"{item}_count"
        if feature_name in feature_data:
            feature_data[feature_name] = count

    return feature_data


# load your models
models = {
    "Support Vector Machine": joblib.load("models/svm_model_generic_img_cls.pkl"),
    "Multi-layer Perceptron": joblib.load("models/mlp_model_generic_img_cls.pkl"),
    "Random Forest": joblib.load("models/rf_model_generic_img_cls.pkl"),
    "Decision Tree": joblib.load("models/dt_model_generic_img_cls.pkl"),
    "K-Nearest Neighbor": joblib.load("models/knn_model_generic_img_cls.pkl"),
}

# initialize the Dash app
app = Dash(__name__)

# define the layout of the app
app.layout = html.Div(
    [
        html.H1("Rental Interest Level Prediction", style={"textAlign": "center"}),
        html.Label("Select Model"),
        dcc.Dropdown(
            id="model_selector",
            options=[{"label": key, "value": key} for key in models.keys()],
            value="Support Vector Machine",
        ),
        # image upload component
        dcc.Upload(
            id="upload-image",
            children=html.Div(["Drag and Drop or ", html.A("Select Image(s)")]),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            # allow multiple files to be uploaded
            multiple=True,
        ),
        html.Div(id="upload-feedback"),
        html.Div(id="detected_items_output"),
        # slider for each feature
        html.Label("Number of Bathrooms"),
        dcc.Slider(
            id="bathrooms_slider",
            min=0,
            max=10,
            step=0.5,
            value=1,
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        html.Label("Number of Bedrooms"),
        dcc.Slider(
            id="bedrooms_slider",
            min=0,
            max=8,
            step=0.5,
            value=1,
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        html.Label("Estimated Price"),
        dcc.Slider(
            id="price_slider",
            min=43,
            max=13000,
            step=100,
            value=3000,
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        html.Label("Description Sentiment"),
        dcc.RadioItems(
            id="description_slider",
            options=[
                {"label": "Positive", "value": 1},
                {"label": "Neutral", "value": 0},
                {"label": "Negative", "value": -1},
            ],
            value=1,
        ),
        html.Label("Has Laundry"),
        dcc.RadioItems(
            id="laundry_slider",
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 0},
            ],
            value=1,
        ),
        html.Label("Has Dishwasher"),
        dcc.RadioItems(
            id="dishwasher_slider",
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 0},
            ],
            value=1,
        ),
        html.Label("Has Hardwood Floors"),
        dcc.RadioItems(
            id="hardwood_slider",
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 0},
            ],
            value=1,
        ),
        html.Label("Allow Dog"),
        dcc.RadioItems(
            id="dog_slider",
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 0},
            ],
            value=1,
        ),
        html.Label("Allow Cat"),
        dcc.RadioItems(
            id="cat_slider",
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 0},
            ],
            value=1,
        ),
        html.Label("Has Doorman"),
        dcc.RadioItems(
            id="doorman_slider",
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 0},
            ],
            value=1,
        ),
        html.Label("Has Elevator"),
        dcc.RadioItems(
            id="elevator_slider",
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 0},
            ],
            value=1,
        ),
        html.Label("Has Application Fee"),
        dcc.RadioItems(
            id="fee_slider",
            options=[
                {"label": "Yes", "value": 1},
                {"label": "No", "value": 0},
            ],
            value=1,
        ),
        html.Label("Has Fitness Center"),
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
        html.Div(id="prediction_output"),
    ]
)


@app.callback(
    [
        Output("prediction_output", "children"),
        Output("detected_items_output", "children"),
    ],
    [Input("predict_button", "n_clicks"), Input("upload-image", "contents")],
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
    list_of_contents,
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
        # check if an image has been uploaded
        if list_of_contents is None:
            return html.Div(
                "Please upload an image to make a prediction.", style={"color": "red"}
            )

        # process the uploaded image - feature extraction
        image_features = process_image(list_of_contents[0], interested_features)

        # create a DataFrame for the input features
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
            "chair_count",
            "sink_count",
            "oven_count",
            "refrigerator_count",
            "toilet_count",
            "person_count",
            "potted plant_count",
            "microwave_count",
            "bottle_count",
            "tv_count",
        ]

        # create a DataFrame for the input features
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
                    *image_features.values(),
                ]
            ],
            columns=cols,
        )

        # prediction
        model = models[selected_model]
        prediction = model.predict(input_data)
        interest_level = {1: "High", 0: "Medium", -1: "Low"}
        prediction_result = f"Predicted Interest Level: {interest_level[prediction[0]]}"

        detected_items_list = [
            html.Li(f"{feature.replace('_count', '')}: {image_features[feature]}")
            for feature in interested_features
        ]
        detected_items_output = html.Ul(children=detected_items_list)

        return prediction_result, detected_items_output

    return "", ""


@app.callback(
    Output("upload-feedback", "children"), [Input("upload-image", "contents")]
)
def update_upload_feedback(list_of_contents):
    if list_of_contents is not None:
        return "Image attached"
    return "Drag and Drop or Click to Select Image (s)"


# run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)
