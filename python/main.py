import pandas as pd
import matplotlib.pyplot as plt

#small sample dataset expand later mayb
data = pd.DataFrame({
    'date': pd.date_range(start='06-20-2024', periods=10, freq='D'),
    'value': [10, 12, 13, 15, 14, 17, 18, 20, 19, 21]
})

print("Sample Dataset:")
print(data)

data.dropna(inplace=True)
summary = data.describe()

print("\nSummary Statistics:")
print(summary)


data.to_csv('../processed_data.csv', index=False)

plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['value'])
plt.title('Data Visualization')
plt.xlabel('Date')
plt.ylabel('Value')
plt.savefig('../data_visualization.png')
plt.show()
