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

sampled_df = df_filtered[["bedrooms", "bathrooms", "price"]].sample(n=1000)

# 3d plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
scatter = ax.scatter(
    sampled_df["bedrooms"], sampled_df["bathrooms"], sampled_df["price"], label="Price"
)
ax.set_xlabel("Bedrooms")
ax.set_ylabel("Bathrooms")
ax.set_zlabel("Price")
plt.title("3D Plot of Price by Bedrooms and Bathrooms")
ax.legend([scatter], ["Price"])
plt.show()
