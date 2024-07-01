import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('fear-greed.csv')

# Check the column names to ensure correct reference
print(df.columns)

# Extract the relevant column (assuming it's named 'fear greed' exactly)
values = df['Fear Greed']

# Check for missing values and handle if any
if values.isnull().sum() > 0:
    values = values.dropna()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(values, bins=20, kde=True)
plt.title('Distribution of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Descriptive statistics
stats = values.describe()
print(stats)
