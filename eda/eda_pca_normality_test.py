# import libraries
import numpy as np
import pandas as pd
from collections import Counter
import re
import os

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from numpy.linalg import svd
import scipy.stats as st

import warnings

warnings.filterwarnings("ignore")

# import the dataset (this dataset has already remove outlier)
df = pd.read_json("../data/sentimental_extraction_kaggle.json")
df.head(5)

print(f"There are {len(df)} samples.")

# check the first 3 row's features list
print(df.features.iloc[0])
print(df.features.iloc[1])
print(df.features.iloc[2])

# flatten the list of features from all rows
all_features = [feature for sublist in df["features"] for feature in sublist]

# count the frequency of each feature
feature_counts = Counter(all_features)

# filter features that have a frequency above the threshold
frequency_threshold = 10000
high_freq_features = [
    feature for feature, count in feature_counts.items() if count >= frequency_threshold
]

# create binary columns for each high-frequency feature
for feature in high_freq_features:
    df["feature_" + feature.lower()] = df["features"].apply(
        lambda x: 1 if feature in x else 0
    )

print(f"The features with most (>= 10k) counts are {high_freq_features}")

# convert target interest_level from categorical to numerical
interest_level_mapping = {"high": 1, "medium": 0, "low": -1}
df["interest_level"] = df["interest_level"].map(interest_level_mapping)

# extract numerical features
final_df = df[
    [
        "bathrooms",
        "bedrooms",
        "price",
        "sentiment_label",
        "feature_laundry in building",
        "feature_dishwasher",
        "feature_hardwood floors",
        "feature_dogs allowed",
        "feature_cats allowed",
        "feature_doorman",
        "feature_elevator",
        "feature_no fee",
        "feature_fitness center",
        "interest_level",
    ]
]

# standardize the dataset
scaler = StandardScaler()
df_standardized = scaler.fit_transform(final_df)

# perform PCA without limiting the number of components to preserve all the variance
pca = PCA()
pca.fit(df_standardized)

# find the number of components required to explain at least 95% variance
cumulative_variance = np.cumsum(pca.explained_variance_ratio_)
num_components = (
    np.argmax(cumulative_variance >= 0.95) + 1
)  # adding 1 because of 0-based indexing

# number of features to be removed
num_features_removed = df_standardized.shape[1] - num_components

# perform PCA again, this time with the desired number of components
pca_reduced = PCA(n_components=num_components)
pca_reduced.fit(df_standardized)

print(f"Number of features to be removed: {num_features_removed}")
print(
    "Explained Variance Ratio of Original Feature Space:", pca.explained_variance_ratio_
)
print(
    "Explained Variance Ratio of Reduced Feature Space:",
    pca_reduced.explained_variance_ratio_,
)

# calculate the cumulative explained variance
cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

# plotting the cumulative explained variance
plt.figure(figsize=(10, 7))
plt.plot(
    range(1, len(cumulative_variance) + 1),
    cumulative_variance,
    marker="o",
    linestyle="--",
)
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance (%)")
plt.title("Cumulative Explained Variance vs. Number of Components")

# drawing the vertical and horizontal dashed lines for 95% variance
optimum_components = np.argmax(cumulative_variance >= 0.95) + 1
plt.axvline(
    x=optimum_components,
    color="black",
    linestyle="--",
    label=f"Optimum Components = {optimum_components}",
)
plt.axhline(y=0.95, color="red", linestyle="--", label="95% Variance")

plt.legend()
plt.grid(True)
plt.show()

# perform K-S test for normality on bedrooms
ks_statistic_bedrooms, ks_pvalue_bedrooms = st.kstest(
    final_df["bedrooms"],
    "norm",
    args=(final_df["bedrooms"].mean(), final_df["bedrooms"].std()),
)

# perform K-S test for normality on bathrooms
ks_statistic_bathrooms, ks_pvalue_bathrooms = st.kstest(
    final_df["bathrooms"],
    "norm",
    args=(final_df["bathrooms"].mean(), final_df["bathrooms"].std()),
)

print(
    f"K-S test: statistics={ks_statistic_bedrooms:.2f} p-value={ks_pvalue_bedrooms:.2f}"
)
print(
    f"K-S test: Number of bedrooms looks {'normal' if ks_pvalue_bedrooms > 0.01 else 'not normal'} with 99% accuracy"
)
print(
    f"K-S test: statistics={ks_statistic_bathrooms:.2f} p-value={ks_pvalue_bathrooms:.2f}"
)
print(
    f"K-S test: Number of bathrooms looks {'normal' if ks_pvalue_bathrooms > 0.01 else 'not normal'} with 99% accuracy"
)

# perform Shapiro-Wilk test for normality on bedrooms
shapiro_statistic_bedrooms, shapiro_pvalue_bedrooms = st.shapiro(final_df["bedrooms"])

# perform Shapiro-Wilk test for normality on bathrooms
shapiro_statistic_bathrooms, shapiro_pvalue_bathrooms = st.shapiro(
    final_df["bathrooms"]
)

print(
    f"Shapiro-Wilk test: statistics={shapiro_statistic_bedrooms:.2f} p-value={shapiro_pvalue_bedrooms:.2f}"
)
print(
    f"Shapiro-Wilk test: Number of bedrooms looks {'normal' if shapiro_pvalue_bedrooms > 0.01 else 'not normal'} with 99% accuracy"
)
print(
    f"Shapiro-Wilk test: statistics={shapiro_statistic_bathrooms:.2f} p-value={shapiro_pvalue_bathrooms:.2f}"
)
print(
    f"Shapiro-Wilk test: Number of bathrooms looks {'normal' if shapiro_pvalue_bathrooms > 0.01 else 'not normal'} with 99% accuracy"
)

# perform DA test for normality on bedrooms
da_statistic_bedrooms, da_pvalue_bedrooms = st.normaltest(final_df["bedrooms"])

# perform DA test for normality on bathrooms
da_statistic_bathrooms, da_pvalue_bathrooms = st.normaltest(final_df["bathrooms"])

print(
    f"D'Agostino's K^2 test: statistics={da_statistic_bedrooms:.2f} p-value={da_pvalue_bedrooms:.2f}"
)
print(
    f"D'Agostino's K^2 test: Number of bedrooms looks {'normal' if da_pvalue_bedrooms > 0.01 else 'not normal'} with 99% accuracy"
)
print(
    f"D'Agostino's K^2 test: statistics={da_statistic_bathrooms:.2f} p-value={da_pvalue_bathrooms:.2f}"
)
print(
    f"D'Agostino's K^2 test: Number of bathrooms looks {'normal' if da_pvalue_bathrooms > 0.01 else 'not normal'} with 99% accuracy"
)
