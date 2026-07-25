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

# reg plot
sns.regplot(x='bathrooms', y='price', data=df_filtered, scatter=True, fit_reg=True)
plt.title('Regression Plot with Scatter Representation')
plt.xlabel('Bathrooms')
plt.ylabel('Price')
plt.show()
```