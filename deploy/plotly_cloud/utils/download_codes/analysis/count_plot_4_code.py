rental_gpt_dash  # import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# import the dataset
url = (
    "https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/data/train.json"
)
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

# create new date columns
df_filtered["day"] = pd.to_datetime(
    df_filtered["created"]
).dt.day  # The day of the datetime.

# count plot
fig = plt.figure(figsize=(12, 6))
sns.countplot(
    x="day",
    hue="interest_level",
    hue_order=["low", "medium", "high"],
    data=df_filtered,
)
plt.title("Bar Chart of Interest Level in Day")
plt.xlabel("Day")
plt.ylabel("Interest Level Counts")
plt.show()
