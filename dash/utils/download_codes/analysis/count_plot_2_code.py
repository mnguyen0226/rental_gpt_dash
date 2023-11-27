# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# import the dataset
url = "https://raw.githubusercontent.com/mnguyen0226/two_sigma_property_listing/main/data/train.json"
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

# create new date columns
df_filtered["date"] = pd.to_datetime(
    df_filtered["created"]
).dt.date  # Returns numpy array of python datetime.date objects.
df_filtered["year"] = pd.to_datetime(
    df_filtered["created"]
).dt.year  # The year of the datetime.
df_filtered["month"] = pd.to_datetime(
    df_filtered["created"]
).dt.month  # The month as January=1, December=12.
df_filtered["day"] = pd.to_datetime(
    df_filtered["created"]
).dt.day  # The day of the datetime.
df_filtered["hour"] = pd.to_datetime(
    df_filtered["created"]
).dt.hour  # The hours of the datetime.
df_filtered["weekday"] = pd.to_datetime(
    df_filtered["created"]
).dt.weekday  # The day of the week with Monday=0, Sunday=6.
df_filtered["quarter"] = pd.to_datetime(
    df_filtered["created"]
).dt.quarter  # The quarter of the date.

# count plot
fig = plt.figure(figsize=(12, 6))
sns.countplot(
    x="year",
    hue="interest_level",
    hue_order=["low", "medium", "high"],
    data=df_filtered,
)
plt.title("Bar Chart of Interest Level in Year")
plt.xlabel("Year")
plt.ylabel("Interest Level Counts")
plt.show()