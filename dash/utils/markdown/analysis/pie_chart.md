```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import the dataset
url = "https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/data/train.json"
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

# plot pie chart
df_interest_split = df.interest_level.value_counts().values
df_interest_label = ["low", "medium", "high"]
explode = (0.1, 0, 0)
plt.pie(df_interest_split, explode=explode, labels=df_interest_label, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Percentages of Interests")
plt.legend(df_interest_label, loc="best")
plt.show()
```