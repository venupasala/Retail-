import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("SampleSuperstore.csv")
df.head()

# Shape of the dataset
df.shape

# Descriptive statistics
df.describe()

# Data types of each column
df.dtypes
category_profit = df.groupby('Category')['Profit'].sum()
print(category_profit)

# Profit by Sub-Category
subcategory_profit = df.groupby('Sub-Category')['Profit'].sum()
print(subcategory_profit)

# Profit by Region
region_profit = df.groupby('Region')['Profit'].sum()
print(region_profit)

# Profit by State
state_profit = df.groupby('State')['Profit'].sum()
print(state_profit)
plt.figure(figsize=(10,5))
sns.barplot(x=category_profit.index, y=category_profit.values)
plt.xlabel('Category')
plt.ylabel('Profit')
plt.title('Profit by Category')
plt.show()

# Heatmap of correlation between numerical columns
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()