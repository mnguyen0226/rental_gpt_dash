```python
# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import statsmodels.api as sm
sns.set(style="whitegrid", color_codes=True)
sns.set(font_scale=1)

# import the dataset
url = "https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/data/train.json"
df = pd.read_json(url)

# outlier removal
upper_bound = np.percentile(df["price"].values, 99)
df_filtered = df[df["price"] <= upper_bound]

# qq plot
prices = np.log1p(df_filtered['price'])
sm.qqplot(prices, line ='45', fit=True, label="log-price")
plt.title('QQ Plot of Log-transformed Prices')
plt.legend()
plt.show()
```