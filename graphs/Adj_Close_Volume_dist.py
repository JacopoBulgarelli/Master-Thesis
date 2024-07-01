import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('complete.csv')

# Plot Adjusted Close prices
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Adj Close'], label='Adjusted Close')
plt.title('Adjusted Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.show()

# Plot Volume
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Volume'], label='Volume', color='orange')
plt.title('Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# Summary statistics for Adjusted Close prices
adj_close_summary = data['Adj Close'].describe()
print("Summary Statistics for Adjusted Close Prices:\n", adj_close_summary)

# Summary statistics for Volume
volume_summary = data['Volume'].describe()
print("\nSummary Statistics for Volume:\n", volume_summary)
