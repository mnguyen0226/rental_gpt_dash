# dash imports
import dash
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import dash_bootstrap_components as dbc
import sqlite3
import plotly.express as px
import pandas as pd

# file imports
from maindash import my_app


#######################################
# Layout
#######################################
def listing_layout():
    layout = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="https://images.unsplash.com/photo-1641160858304-6aded85fa2c4?q=80&w=1332&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
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
                        "New York City Apartments Listing",
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
            # Map Display Area
            html.Div(
                dcc.Graph(id="listing_map_display"),
                style={"width": "100%", "height": "500px"},
            ),
            html.Div(
                style={"display": "flex"},
                children=[
                    html.Div(
                        style={
                            "width": "20%",
                            "padding": "10px",
                        },
                        children=[
                            left_side(),
                        ],
                    ),
                    html.Div(
                        style={
                            "width": "80%",
                            "padding": "10px",
                        },
                        children=[
                            right_side(),
                        ],
                    ),
                ],
            ),
        ]
    )

    return layout


def left_side():
    return html.Div(
        [
            html.Div(
                [
                    html.Label("Number of Bathrooms"),
                    dcc.Slider(
                        id="listing_bathrooms_filter",
                        min=0,
                        max=5,
                        step=0.5,
                        value=1,
                        marks=None,
                        tooltip={"placement": "bottom", "always_visible": True},
                    ),
                    html.Br(),
                    html.Label("Number of Bedrooms"),
                    dcc.Slider(
                        id="listing_bedrooms_filter",
                        min=0,
                        max=5,
                        step=1,
                        value=1,
                        marks=None,
                        tooltip={"placement": "bottom", "always_visible": True},
                    ),
                    html.Br(),
                    html.Label("Sort by Price"),
                    dcc.Dropdown(
                        id="listing_price_sorting",
                        options=[
                            {"label": "No Sorting", "value": "none"},
                            {"label": "Low to High", "value": "asc"},
                            {"label": "High to Low", "value": "desc"},
                        ],
                        value="none",
                    ),
                    html.Br(),
                    html.Label("Filtered by Features"),
                    dcc.Checklist(
                        id="listing_features_filter",
                        options=[
                            {
                                "label": "Laundry in Building",
                                "value": "feature_laundry_in_building",
                            },
                            {"label": "Dishwasher", "value": "feature_dishwasher"},
                            {
                                "label": "Hardwood Floors",
                                "value": "feature_hardwood_floors",
                            },
                            {"label": "Dogs Allowed", "value": "feature_dogs_allowed"},
                            {"label": "Cats Allowed", "value": "feature_cats_allowed"},
                            {"label": "Doorman", "value": "feature_doorman"},
                            {"label": "Elevator", "value": "feature_elevator"},
                            {
                                "label": "Fitness Center",
                                "value": "feature_fitness_center",
                            },
                        ],
                        value=["feature_laundry_in_building"],
                    ),
                ],
                style={"display": "flex", "flexDirection": "column", "padding": "10px"},
            )
        ]
    )


def right_side():
    return html.Div(
        [
            dcc.Loading(
                id="loading-cards",
                children=[html.Div(id="listing_cards_container")],
                type="circle",
            )
        ]
    )


def query_database(filters):
    con = sqlite3.connect("database.db")
    query = """
    SELECT * FROM properties
    WHERE bathrooms BETWEEN ? AND ?
      AND bedrooms BETWEEN ? AND ?
      AND {}  -- this will be formatted with the correct string for features
    """

    # handling binary feature filters
    feature_conditions = []
    for feature in filters["features"]:
        feature_conditions.append(f'"{feature}" = 1')
    feature_query = " AND ".join(feature_conditions) if feature_conditions else "1=1"

    # formatting the query with the feature conditions
    query = query.format(feature_query)

    df = pd.read_sql_query(
        query,
        con,
        params=[
            filters["bathrooms"][0],
            filters["bathrooms"][1],
            filters["bedrooms"][0],
            filters["bedrooms"][1],
        ],
    )

    # categorize the listings into terciles
    terciles = df["price"].quantile([1 / 3, 2 / 3]).tolist()

    def categorize_price(price):
        if price <= terciles[0]:
            return "Poor"
        elif price <= terciles[1]:
            return "Median"
        else:
            return "Rich"

    df["price_category"] = df["price"].apply(categorize_price)

    con.close()
    return df


@my_app.callback(
    [
        Output("listing_cards_container", "children"),
        Output("listing_map_display", "figure"),
    ],
    [
        Input("listing_bathrooms_filter", "value"),
        Input("listing_bedrooms_filter", "value"),
        Input("listing_features_filter", "value"),
        Input("listing_price_sorting", "value"),  # Add input for sorting
    ],
)
def update_content(bathrooms, bedrooms, features, sort_order):
    filters = {
        "bathrooms": [bathrooms, bathrooms + 0.5],
        "bedrooms": [bedrooms, bedrooms],
        "features": features,
    }
    filtered_df = query_database(filters)

    # apply sorting based on user selection
    if sort_order == "asc":
        filtered_df = filtered_df.sort_values(by="price", ascending=True)
    elif sort_order == "desc":
        filtered_df = filtered_df.sort_values(by="price", ascending=False)

    # create cards and update map as before
    cards_content = html.Div(
        create_cards(filtered_df), style={"display": "flex", "flexWrap": "wrap"}
    )
    fig = px.scatter_mapbox(
        filtered_df,
        lat="latitude",
        lon="longitude",
        zoom=10,
        center=dict(lat=40.7128, lon=-74.0060),
        mapbox_style="open-street-map",
        height=500,
    )

    return cards_content, fig


def create_cards(df):
    cards = []
    for _, row in df.iterrows():
        # define header color based on price category
        header_color, money_bags = {
            "Poor": ("lightgreen", "💰"),  # 1 money bag for Poor
            "Median": ("lightblue", "💰💰"),  # 2 money bags for Median
            "Rich": ("salmon", "💰💰💰"),  # 3 money bags for Rich
        }.get(row["price_category"], ("lightgrey", ""))

        header_style = {"backgroundColor": header_color}

        # truncate the description to 100 characters to standardize card size
        description = (
            row["description"]
            if len(row["description"]) <= 100
            else row["description"][:100] + "..."
        )

        card_content = [
            dbc.CardHeader(
                [
                    html.Span(f"ID: {row['listing_id']}", style={"flexGrow": 1}),
                    html.Span(money_bags, style={"marginLeft": "20px"}),
                ],
                style=header_style,
            ),
            dbc.CardBody(
                [
                    html.H5(f"🏡 {row['street_address']}", className="card-title"),
                    html.P([html.Strong("About: "), f"{description}"]),
                    html.P([html.Strong("Price: "), f"${row['price']}"]),
                    html.P([html.Strong("Bathrooms: "), f"{row['bathrooms']}"]),
                    html.P([html.Strong("Bedrooms: "), f"{row['bedrooms']}"]),
                ]
            ),
        ]
        cards.append(dbc.Card(card_content, style={"width": "18rem", "margin": "10px"}))
    return cards
