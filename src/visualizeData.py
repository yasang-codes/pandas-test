import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/employees-pandas.csv')

df.plot()

plt.show()