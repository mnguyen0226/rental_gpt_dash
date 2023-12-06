# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
from prettytable import PrettyTable

sns.set(style="whitegrid", color_codes=True)
sns.set(font_scale=1)

import warnings

warnings.filterwarnings("ignore")

# import the dataset
df = pd.read_json("../data/train.json")
df.head(5)

# price scatter plot
df_price = df["price"].values
plt.scatter(range(df.shape[0]), df_price)
plt.title("Scatter Plot of Renting Prices")
plt.xlabel("Property Index")
plt.ylabel("Price")
plt.show()

# similarly, we can do a boxen plot for outlier detection
sns.boxenplot(y="price", data=df)
plt.plot([], label="Price Distribution", color="blue")
plt.title("Boxen Plot of Prices")
plt.ylabel("Price")
plt.legend()
plt.show()

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

plt.scatter(range(df_filtered.shape[0]), df_filtered["price"], label="Prices")
plt.title("Scatter Plot of Renting Prices Without Outliers")
plt.xlabel("Property Index")
plt.ylabel("Price")
plt.legend(loc="best")
plt.show()

# similarly, we can do a boxen plot for outlier detection
sns.boxenplot(y="price", data=df_filtered)
plt.plot([], label="Price Distribution", color="blue")
plt.title("Boxen Plot of Prices Without Outliers")
plt.ylabel("Price")
plt.legend()
plt.show()

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

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtered, x="date", y="price", label="Price")
plt.title("Line Plot of Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

bedroom_counts = df_filtered["bedrooms"].value_counts()
plt.bar(bedroom_counts.index, bedroom_counts.values, label="Bedroom Counts")
plt.title("Bar Chart of Number of Bedrooms Counts")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Number of Occurence")
plt.legend()
plt.show()

bathroom_counts = df_filtered["bathrooms"].value_counts()
plt.bar(bedroom_counts.index, bedroom_counts.values, label="Bathroom Counts")
plt.title("Bar Chart of Number of Bathrooms Counts")
plt.xlabel("Number of Bathrooms")
plt.ylabel("Number of Occurence")
plt.legend()
plt.show()

fig = plt.figure(figsize=(12, 6))
sns.countplot(
    x="hour",
    hue="interest_level",
    hue_order=["low", "medium", "high"],
    data=df_filtered,
)
plt.title("Bar Chart of Interest Level in 24 Hours")
plt.xlabel("Hour")
plt.ylabel("Interest Level Counts")
plt.show()

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

fig = plt.figure(figsize=(12, 6))
sns.countplot(
    x="month",
    hue="interest_level",
    hue_order=["low", "medium", "high"],
    data=df_filtered,
)
plt.title("Bar Chart of Interest Level in Month")
plt.xlabel("Month")
plt.ylabel("Interest Level Counts")
plt.show()

fig = plt.figure(figsize=(12, 6))
sns.countplot(
    x="day", hue="interest_level", hue_order=["low", "medium", "high"], data=df_filtered
)
plt.title("Bar Chart of Interest Level in Day")
plt.xlabel("Day")
plt.ylabel("Interest Level Counts")
plt.show()

fig = plt.figure(figsize=(12, 6))
sns.countplot(
    x="weekday",
    hue="interest_level",
    hue_order=["low", "medium", "high"],
    data=df_filtered,
)
plt.title("Bar Chart of Interest Level in Weekday")
plt.xlabel("Weekday")
plt.ylabel("Interest Level Counts")
plt.show()

fig = plt.figure(figsize=(12, 6))
sns.countplot(
    x="quarter",
    hue="interest_level",
    hue_order=["low", "medium", "high"],
    data=df_filtered,
)
plt.title("Bar Chart of Interest Level in Quarter")
plt.xlabel("Quarter")
plt.ylabel("Interest Level Counts")
plt.show()

# plot pie chart
df_interest_split = df.interest_level.value_counts().values
df_interest_label = ["low", "medium", "high"]
explode = (0.1, 0, 0)
plt.pie(
    df_interest_split,
    explode=explode,
    labels=df_interest_label,
    autopct="%1.1f%%",
    shadow=True,
    startangle=140,
)
plt.title("Percentages of Interests")
plt.legend(df_interest_label, loc="best")
plt.show()

sns.distplot(df_filtered["price"])

# add means and variance to plot
plt.axvline(x=df_filtered["price"].mean(), color="r", linestyle="--", label="Mean")
plt.axvline(x=df_filtered["price"].median(), color="g", linestyle="-", label="Median")

plt.title("Distribution Plot of Prices")
plt.xlabel("Price")
plt.ylabel("Distribution")
plt.legend()
plt.show()

sns.pairplot(df_filtered[["bathrooms", "bedrooms", "price"]])
plt.title("Feature Pair Plot")
plt.show()

# get the correlation
corr = df_filtered[["bathrooms", "bedrooms", "price"]].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
cbar = plt.gcf().axes[-1]
plt.title("Correlation Heatmap")
plt.show()

# similarly, histogram plot with KDE
sns.histplot(data=df_filtered, x="price", kde=True)

# add means and variance to plot
plt.axvline(x=df_filtered["price"].mean(), color="r", linestyle="--", label="Mean")
plt.axvline(x=df_filtered["price"].median(), color="g", linestyle="-", label="Median")

plt.title("KDE of Prices")
plt.xlabel("Price")
plt.ylabel("Density")
plt.legend()
plt.show()

prices = np.log1p(df_filtered["price"])
sm.qqplot(prices, line="45", fit=True, label="log-price")
plt.title("QQ Plot of Log-transformed Prices")
plt.legend()
plt.show()

sns.kdeplot(df_filtered["price"], fill=True, alpha=0.6, linewidth=2)

# add means and variance to plot
plt.axvline(x=df_filtered["price"].mean(), color="r", linestyle="--", label="Mean")
plt.axvline(x=df_filtered["price"].median(), color="g", linestyle="-", label="Median")

plt.title("KDE of Prices")
plt.xlabel("Price")
plt.ylabel("Density")
plt.legend()
plt.show()

sns.regplot(x="bathrooms", y="bedrooms", data=df_filtered, scatter=True, fit_reg=True)
plt.title("Regression Plot with Scatter Representation")
plt.xlabel("Bathrooms")
plt.ylabel("Bedrooms")
plt.show()

sns.regplot(x="bathrooms", y="price", data=df_filtered, scatter=True, fit_reg=True)
plt.title("Regression Plot with Scatter Representation")
plt.xlabel("Bathrooms")
plt.ylabel("Price")
plt.show()

sns.regplot(x="bedrooms", y="price", data=df_filtered, scatter=True, fit_reg=True)
plt.title("Regression Plot with Scatter Representation")
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.show()

df_filtered["date"] = pd.to_datetime(df_filtered["created"]).dt.date
grouped = df_filtered.groupby(["date", "interest_level"])["price"].mean().reset_index()
pivot_df = grouped.pivot(index="date", columns="interest_level", values="price")
pivot_df.plot(kind="area", stacked=False, alpha=0.5, figsize=(12, 6))
plt.title("Area Plot of Prices Over Time by Interest Level")
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.show()

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

sns.jointplot(
    data=df_filtered,
    x="price",
    y="bathrooms",
    hue="interest_level",
    kind="scatter",
    color="b",
).plot_joint(sns.kdeplot, zorder=0, levels=6)
plt.xlabel("Prices")
plt.ylabel("Number of Bathrooms")
plt.show()

sns.rugplot(data=df_filtered, x="price", height=0.5)

# add means and variance to plot
plt.axvline(x=df_filtered["price"].mean(), color="r", linestyle="--", label="Mean")
plt.axvline(x=df_filtered["price"].median(), color="g", linestyle="-", label="Median")

plt.title("Rug Plot of Prices")
plt.xlabel("Price")
plt.ylabel("Density")
plt.legend()
plt.show()

sampled_df = df_filtered[["bedrooms", "bathrooms", "price"]].sample(n=1000)

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

xi = np.linspace(sampled_df["bathrooms"].min(), sampled_df["bathrooms"].max(), 100)
yi = np.linspace(sampled_df["bedrooms"].min(), sampled_df["bedrooms"].max(), 100)
zi = griddata(
    (sampled_df["bathrooms"], sampled_df["bedrooms"]),
    sampled_df["price"],
    (xi[None, :], yi[:, None]),
    method="linear",
)

fig = plt.figure(figsize=(10, 8))
contour = plt.contourf(xi, yi, zi, 14, cmap=plt.cm.RdBu_r)
plt.colorbar(contour, label="Price")
plt.xlabel("Bathrooms")
plt.ylabel("Bedrooms")
plt.title("Contour Plot of Price by Bedrooms and Bathrooms")
plt.show()

x = df["bedrooms"]
y = df["bathrooms"]
z = df["price"]

# create grid values first
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# interpolate
zi = griddata((x, y), z, (xi, yi), method="cubic")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# plot the surface.
surf = ax.contourf(xi, yi, zi, 50, cmap="viridis", extend3d=True)

ax.set_xlabel("Bedrooms")
ax.set_ylabel("Bathrooms")
ax.set_zlabel("Price")
cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.set_label("Price")

plt.title("3D Contour Plot of Price by Bedrooms and Bathrooms")
plt.show()

numerical_cols = ["bathrooms", "bedrooms", "latitude", "longitude", "price"]
df_numerical = df_filtered[numerical_cols]
df_numerical = df_numerical.dropna()
sns.clustermap(
    df_numerical, method="average", cmap="coolwarm", standard_scale=1, figsize=(10, 10)
)
plt.show()

df_zoomed = df_filtered[
    (df_filtered["latitude"] > 40.7)
    & (df_filtered["latitude"] < 40.8)
    & (df_filtered["longitude"] > -74)
    & (df_filtered["longitude"] < -73.9)
]

plt.hexbin(
    df_zoomed["longitude"], df_zoomed["latitude"], gridsize=50, cmap="Blues", mincnt=1
)
cb = plt.colorbar(label="count in bin")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Zoomed Hexbin of Listings by Latitude and Longitude")
plt.xlim(-74, -73.9)
plt.ylim(40.7, 40.8)
plt.show()

df_interest_label = ["low", "medium", "high"]
sns.stripplot(x="interest_level", y="price", data=df_filtered, hue="price")
plt.ylabel("Price")
plt.xlabel("Interest Level")
plt.title("Price vs. Interest Level")
plt.show()

df_interest_label = ["low", "medium", "high"]
sns.stripplot(x="bedrooms", y="price", data=df_filtered, hue="price")
plt.ylabel("Price")
plt.xlabel("Bedrooms")
plt.title("Bedrooms vs. Interest Level")
plt.show()

df_interest_label = ["low", "medium", "high"]
sns.stripplot(x="bathrooms", y="price", data=df_filtered, hue="price")
plt.ylabel("Price")
plt.xlabel("Bathrooms")
plt.title("Bathrooms vs. Interest Level")
plt.show()

df_sampled = df_filtered[df_filtered["price"] < 2000]  # Adjust the range as needed

sns.swarmplot(x="interest_level", y="price", data=df_sampled)

plt.title("Swarm Plot of Prices by Interest Level")
plt.xlabel("Interest Level")
plt.ylabel("Price")

plt.show()

fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Price vs Interest Level
df_interest_label = ["low", "medium", "high"]
sns.boxplot(ax=axs[0, 0], x="interest_level", y="price", data=df_filtered)
axs[0, 0].set_title("Price Distribution by Interest Level")
axs[0, 0].set_xlabel("Interest Level")
axs[0, 0].legend(df_interest_label, loc="best")
axs[0, 0].set_ylabel("Price")

# Bedrooms vs Interest Level
sns.countplot(ax=axs[0, 1], x="bedrooms", hue="interest_level", data=df_filtered)
axs[0, 1].set_title("Bedroom Count by Interest Level")
axs[0, 1].set_xlabel("Number of Bedrooms")
axs[0, 1].set_ylabel("Count")

# Bathrooms vs Interest Level
sns.countplot(ax=axs[1, 0], x="bathrooms", hue="interest_level", data=df_filtered)
axs[1, 0].set_title("Bathroom Count by Interest Level")
axs[1, 0].set_xlabel("Number of Bathrooms")
axs[1, 0].set_ylabel("Count")

# Violin plot of interest rate vs price
sns.violinplot(
    ax=axs[1, 1],
    x="interest_level",
    y="price",
    order=["low", "medium", "high"],
    data=df_filtered[df_filtered.price <= df_filtered.price.quantile(0.99)],
)
axs[1, 1].set_title("Violin Plot of Interest Rate vs. Price")
axs[1, 1].set_xlabel("Interest Level")
axs[1, 1].set_ylabel("Price")

fig.suptitle("Exploratory Data Analysis")
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Percentage of interest level
df_interest_split = df.interest_level.value_counts().values
df_interest_label = ["low", "medium", "high"]
explode = (0.1, 0, 0)
axes[0, 0].pie(
    df_interest_split,
    explode=explode,
    labels=df_interest_label,
    autopct="%1.1f%%",
    shadow=True,
    startangle=140,
)
axes[0, 0].set_title("Percentages of Interests")
axes[0, 0].grid(True)

# Count of listings by number of bedrooms and interest level
sns.barplot(
    x="bedrooms",
    y="price",
    data=df_filtered,
    label="Average Price of Bedrooms",
    ax=axes[0, 1],
)
axes[0, 1].set_title("Average Price by Number of Bedrooms")
axes[0, 1].legend()
axes[0, 1].grid(True)

# Count of listings by number of bathrooms and interest level
sns.barplot(
    x="bathrooms",
    y="price",
    data=df_filtered,
    label="Average Price of Bathrooms",
    ax=axes[1, 0],
)
axes[1, 0].set_title("Average Price by Number of Bathrooms")
axes[1, 0].legend()
axes[1, 0].grid(True)

# Scatter plot of price vs latitude
sns.lineplot(data=df_filtered, x="date", y="price", label="Price")
axes[1, 1].set_title("Line Plot of Prices")
axes[1, 1].grid(True)

fig.suptitle("Exploratory Data Analysis")
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Distplot of prices
sns.distplot(df_filtered["price"], ax=axes[0, 0])
axes[0, 0].axvline(
    x=df_filtered["price"].mean(), color="r", linestyle="--", label="Mean"
)
axes[0, 0].axvline(
    x=df_filtered["price"].median(), color="g", linestyle="-", label="Median"
)
axes[0, 0].set_title("Distribution Plot of Prices")
axes[0, 0].legend()
axes[0, 0].grid(True)

# Heatmap of features
corr = df_filtered[["bathrooms", "bedrooms", "price"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, ax=axes[0, 1])
cbar = plt.gcf().axes[-1]
axes[0, 1].set_title("Correlation Heatmap")
axes[0, 1].grid(True)

# Regression plot between bedrooms and price
sns.regplot(
    x="bedrooms", y="price", data=df_filtered, scatter=True, fit_reg=True, ax=axes[1, 0]
)
axes[1, 0].set_title("Regression Plot with Scatter Representation")
axes[1, 0].grid(True)

# Regression plot between bathrooms and price
sns.regplot(
    x="bathrooms",
    y="price",
    data=df_filtered,
    scatter=True,
    fit_reg=True,
    ax=axes[1, 1],
)
axes[1, 1].set_title("Regression Plot with Scatter Representation")
axes[1, 1].grid(True)

fig.suptitle("Exploratory Data Analysis")
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
df_interest_label = ["low", "medium", "high"]

# Hexbin of NYC latitude and longitude
df_zoomed = df_filtered[
    (df_filtered["latitude"] > 40.7)
    & (df_filtered["latitude"] < 40.8)
    & (df_filtered["longitude"] > -74)
    & (df_filtered["longitude"] < -73.9)
]
axes[0, 0].hexbin(
    df_zoomed["longitude"], df_zoomed["latitude"], gridsize=50, cmap="Blues", mincnt=1
)
axes[0, 0].set_title("Zoomed Hexbin of Listings by Latitude and Longitude")
axes[0, 0].set_xlabel("Longitude")
axes[0, 0].set_ylabel("Latitude")
axes[0, 0].grid(True)

# Price vs Interests
sns.stripplot(
    x="interest_level", y="price", data=df_filtered, hue="price", ax=axes[0, 1]
)
axes[0, 1].set_title("Price vs. Interest Level")
axes[0, 1].set_xlabel("Price")
axes[0, 1].set_ylabel("Interest Level")
axes[0, 1].grid(True)

# Price vs Number of Bedrooms
sns.stripplot(x="bedrooms", y="price", data=df_filtered, hue="price", ax=axes[1, 0])
axes[1, 0].set_title("Bedrooms vs. Price")
axes[1, 0].set_xlabel("Bedrooms")
axes[1, 0].set_ylabel("Price")
axes[1, 0].grid(True)

# Price vs Number of Bathrooms
sns.stripplot(x="bathrooms", y="price", data=df_filtered, hue="price", ax=axes[1, 1])
axes[1, 1].set_title("Bathrooms vs. Price")
axes[1, 1].set_xlabel("Bathrooms")
axes[1, 1].set_ylabel("Price")
axes[1, 1].grid(True)

fig.suptitle("Exploratory Data Analysis")
plt.tight_layout()
plt.show()

corr = df_filtered[["bathrooms", "bedrooms", "price"]].corr()
table = PrettyTable()
table.field_names = ["Feature"] + list(corr.columns)
for index, row in corr.iterrows():
    table.add_row([index] + list(row))
print(table)
