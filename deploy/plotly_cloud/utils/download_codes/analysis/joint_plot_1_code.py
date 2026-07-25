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

# joint plot
sns.jointplot(
    data=df_filtered,
    x="price",
    y="bedrooms",
    hue="interest_level",
    kind="scatter",
    color="b",
).plot_joint(sns.kdeplot, zorder=0, levels=6)
plt.xlabel("Prices")
plt.ylabel("Number of Bedrooms")
plt.show()
