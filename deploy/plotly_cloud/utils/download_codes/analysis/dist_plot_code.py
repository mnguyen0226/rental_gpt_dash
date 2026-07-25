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

# dist plot
sns.distplot(df_filtered["price"])

# add means and variance to plot
plt.axvline(x=df_filtered["price"].mean(), color="r", linestyle="--", label="Mean")
plt.axvline(x=df_filtered["price"].median(), color="g", linestyle="-", label="Median")

plt.title("Distribution Plot of Prices")
plt.xlabel("Price")
plt.ylabel("Distribution")
plt.legend()
plt.show()
