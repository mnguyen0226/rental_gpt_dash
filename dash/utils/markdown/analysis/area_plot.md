```python
# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
sns.set(style="whitegrid", color_codes=True)
sns.set(font_scale=1)

# import the dataset
url = "https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/data/train.json"
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

# create the 'date' column to datetime
df_filtered["date"] = pd.to_datetime(df_filtered['created']).dt.date 

# group by date and interest level, and calculate the average price
grouped = df_filtered.groupby(['date', 'interest_level'])['price'].mean().reset_index()

pivot_df = grouped.pivot(index='date', columns='interest_level', values='price')
pivot_df.plot(kind='area', stacked=False, alpha=0.5, figsize=(12, 6))
plt.title('Area Plot of Prices Over Time by Interest Level')
plt.xlabel('Date')
plt.ylabel('Average Price')
plt.show()
```