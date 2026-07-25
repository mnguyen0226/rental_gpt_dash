# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import the dataset
url = (
    "https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/data/train.json"
)
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

# bar plot
bedroom_counts = df_filtered["bedrooms"].value_counts()
plt.bar(bedroom_counts.index, bedroom_counts.values, label="Bedroom Counts")
plt.title("Bar Chart of Number of Bedrooms Counts")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Number of Occurence")
plt.legend()
plt.show()
