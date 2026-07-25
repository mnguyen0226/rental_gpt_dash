```python
# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# import the dataset
url = "https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/data/train.json"
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

# create new date columns
df_filtered["date"] = pd.to_datetime(
    df_filtered["created"]
).dt.date

# line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtered, x="date", y="price", label="Price")
plt.title("Line Plot of Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
```