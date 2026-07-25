# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set(style="whitegrid", color_codes=True)
sns.set(font_scale=1)

# import the dataset
url = (
    "https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/data/train.json"
)
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

# density heatmap by price
interest_level = "low"
# interest_level = "medium"
# interest_level = "high"
medium_interest_df = df_filtered[df_filtered["interest_level"] == interest_level]
fig = px.density_mapbox(
    medium_interest_df,
    lat="latitude",
    lon="longitude",
    z="price",
    radius=8,
    center=dict(lat=40.7128, lon=-74.0060),  # Center on NYC
    zoom=10,  # Zoom level to focus on NYC
    mapbox_style="open-street-map",
)

fig.update_layout(
    title={
        "text": f"Heatmap of NYC Rental Listings Price Based On Interest Level",
        "x": 0.5,
        "xanchor": "center",
    }
)

fig.show()
