import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('--- Series ---')

s = pd.Series(np.random.randn(4), name='daily returns')
print(s)
print()

print(type(s))
print()

print(s * 100)
print()

print(np.abs(s))
print()

print(s.describe())
print()

s.index = ['AMZN', 'AAPL', 'MSFT', 'GOOG']
print(s)
print()

print(s['AMZN'])
print()

s['AMZN'] = 0
print(s)
print()

print('AAPL' in s)
print()

print('--------------------\n')

print('--- DataFrames ---')

df = pd.read_csv('../dataset/salaries.csv')
print(type(df))
print()

print(df)
print()

print('--- Select particular rows using standard Python array slicing notation ---')

print(df[:2])
print()

print('--- Select columns with a bracket call ---')

print(df['Name'])
print(df['Salary'])
print()

print('--- Select multiple columns with a list of column names, Since you are passing in a list, you see two sets of [] ---')

print(df[['Name', 'Salary']])
print()

print('--- Similar to NumPy, you can calls min(), max(), mean(), etc... on a pandas dataframe ---')

print(df['Age'].mean())
print()

print('--- Conditional filtering ---')

print(df['Age'] > 30)
print(df[df['Age'] > 30])
print()

print('--- Get list of unique values for Age ---')

print(df['Age'].unique())
print()

print('--- Get number of unqiue values ---')

print(df['Age'].nunique())
print()

print('--- General info about dataframe ---')

print(df.info())
print()


print('--- Statistics about dataframe ---')

print(df.describe())
print()


print('--- Get a list of all columns ---')

print(df.columns)
print()

print('--- Set dataframe index ---')

df = df.set_index('Name')
print(df)

print('--- Get a list of indices ---')

print(df.index)
print()

print('--- Plot graph using matplotlib ---')

df['Salary'].plot(kind='bar')
plt.show()

print('--- Convert a numpy matrix to a dataframe ---')

mat = np.random.randn(100, 4)
df = pd.DataFrame(mat, columns=['A', 'B', 'C', 'D'])
print(df)

df.plot()
plt.show()

print('--------------------\n')
