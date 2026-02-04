import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 150)

df = pd.read_csv('Pandas-practice/meal_tracker.tsv', sep='\t')

print(df.head())
print(df.info())

# Avg calories per meal vs total calories
avg = df.groupby('Date')['Calories'].mean()
total = df.groupby('Date')['Calories'].sum()

labels = ['Total', 'Avg']
i = 0

fig, ax = plt.subplots(figsize=(12, 6))
for series in [total, avg]:
    bar = ax.bar(series.index, series.values, label=labels[i])
    ax.bar_label(bar, label_type='center')
    i += 1
ax.set_xlabel('Date')
ax.set_ylabel('Calories')
ax.set_title('Daily average calories per meal')
ax.legend()
plt.show()