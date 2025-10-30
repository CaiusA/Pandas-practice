import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 150)


df = pd.read_csv("Pandas-practice/Cities with the Best Work-Life Balance 2022.csv")

df['2021'] = pd.to_numeric(df['2021'], 'coerce').astype('Int64')

df['Overworked Population'] = df['Overworked Population'].str.replace('%', '')
df['Overworked Population'] = pd.to_numeric(df['Overworked Population'])
df['Vacations Taken (Days)'] = pd.to_numeric(df['Vacations Taken (Days)'], 'coerce').fillna(0)

df['Paid Parental Leave (Days)'] = df['Paid Parental Leave (Days)'].str.replace(',', '')
df['Paid Parental Leave (Days)'] = pd.to_numeric(df['Paid Parental Leave (Days)'])

print(df.head())
print(df.info())

# 3 cities with the largest change in ranking
df['Ranking Difference'] = abs(df['2022'] - df['2021'])
print(df[['2022', '2021', 'Ranking Difference', 'City', 'Country']].nlargest(3, 'Ranking Difference'))

# Countries ordered by highest average work-life balance score
countries = df.groupby('Country')['TOTAL SCORE'].mean().sort_values(ascending=False)
print(countries.head())

# Overworked population vs Vacation days taken
fig, ax = plt.subplots()
ax.scatter(df['Overworked Population'], df['Vacations Taken (Days)'])
ax.set_xlabel('Overworked population (%)')
ax.set_ylabel('Vacations Taken (Days)')
ax.set_title('Overworked Pop. vs Vacation Days Taken')
ax.grid(True, linestyle='-.')
plt.show()

# More detailed version where each dot is colored based on the city's work-life balance score
sns.set_theme()
sns.scatterplot(x='Overworked Population', y='Vacations Taken (Days)', data=df,
                hue='TOTAL SCORE').set(title='Overworked Pop. vs Vacation Days Taken')
plt.show()