import pandas as pd

df = pd.read_csv('data/employees-pandas.csv')

df.to_string()

print(df)

print(df.info())