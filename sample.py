
#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/home/pigeon/Documents/UnderstandingPython/gapminder-FiveYearData.csv")

print(df)

print(df.head())

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.info())

# country_df = df['country']

# print(country_df.head)

# print(df.head(n=15))

# print(df.head())

# print(df.shape)

# print(df.columns)

# print(df.dtypes)

# print(df.info())

country_df = df['country']

print(country_df.head)

print(df.head(n=15))
