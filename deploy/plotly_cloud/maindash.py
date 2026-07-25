import os

import dash
import dash_bootstrap_components as dbc
import pandas as pd

my_app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
)
my_app.title = "RentalGPT"
server = my_app.server

# import the dataset: prefer a local copy (present in local checkouts under
# ../data/) to avoid re-fetching ~70MB over the network on every start; the
# Docker image doesn't include ../data/, so deployments fall back to the URL.
_local_data_path = os.path.join(os.path.dirname(__file__), "..", "data", "train.json")
if os.path.exists(_local_data_path):
    df = pd.read_json(_local_data_path)
else:
    url = "https://raw.githubusercontent.com/mnguyen0226/two_sigma_property_listing/main/data/train.json"
    df = pd.read_json(url)
