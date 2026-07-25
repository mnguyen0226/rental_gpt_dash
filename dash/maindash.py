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

# import the dataset, preferring a local copy over the network so cold
# starts don't have to re-fetch ~70MB every time:
#   1. a small bundled sample colocated with this file (used by size-limited
#      deploy packages, e.g. deploy/plotly_cloud/data/train.json)
#   2. the full local dataset under ../data/ (present in local checkouts)
#   3. the remote URL, as a last resort
_sample_data_path = os.path.join(os.path.dirname(__file__), "data", "train.json")
_local_data_path = os.path.join(os.path.dirname(__file__), "..", "data", "train.json")
if os.path.exists(_sample_data_path):
    df = pd.read_json(_sample_data_path)
elif os.path.exists(_local_data_path):
    df = pd.read_json(_local_data_path)
else:
    url = "https://raw.githubusercontent.com/mnguyen0226/two_sigma_property_listing/main/data/train.json"
    df = pd.read_json(url)
