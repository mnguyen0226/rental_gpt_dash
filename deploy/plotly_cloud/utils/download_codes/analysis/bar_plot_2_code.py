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
bathroom_counts = df_filtered["bathrooms"].value_counts()
plt.bar(bathroom_counts.index, bathroom_counts.values, label="Bathroom Counts")
plt.title("Bar Chart of Number of Bathrooms Counts")
plt.xlabel("Number of Bathrooms")
plt.ylabel("Number of Occurence")
plt.legend()
plt.show()
