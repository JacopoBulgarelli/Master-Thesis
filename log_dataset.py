# -*- coding: utf-8 -*-
"""log_dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pj96rQFrqW3x9ZocLKlUT_HvL_1qtuVt
"""

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('dataset.csv')

# List of columns to log-transform
log_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

df['fear-greed'] = df['fear-greed'] / 100

# Apply log transformation to the selected columns (adding 1 to avoid log(0))
df[log_columns] = df[log_columns].apply(lambda x: np.log(x + 1))

# Save the transformed dataset
df.to_csv('transformed_dataset.csv', index=False)

print("Log transformation completed and saved as 'transformed_dataset.csv'")
