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

# violin plot
sns.violinplot(
    x="interest_level",
    y="price",
    order=["low", "medium", "high"],
    data=df_filtered[df_filtered.price <= df_filtered.price.quantile(0.99)],
)
plt.plot([], label="Price Distribution", color="blue")
plt.title("Violin Plot of Interest Rate vs. Price")
plt.xlabel("Interest Level")
plt.ylabel("Price")
plt.legend()
plt.show()
