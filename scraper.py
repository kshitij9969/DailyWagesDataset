
import numpy as np

import tabula

import pandas as pd

file = "AgriWages2016-17.pdf"

df = tabula.read_pdf(file, pages=[34], multiple_tables=True)

import camelot

pages = ''

for i in range(33, 251):
       pages += str(i) + ','

pages = pages[:-1]

tables = camelot.read_pdf(file, pages=pages)

# print(tables[0].df)

camelot.plot(tables[0], kind='grid').show()

df = pd.DataFrame(tables[0].df)
df.columns = df.iloc[0]
df = df[1:]

df = df[['', 'Labour \nCategory', 'Labour \nType', 'July', 'August',
       'September', 'October', 'November', 'December', 'January', 'February',
       'March', 'April', 'May', 'June', 'Annual \nAverage']]

# print(df.columns)
df.columns = ['1', 'Gender', 'Labour Category', 'Labour Type', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'Annual Average']
df.dropna(inplace=True)
df.to_csv('tes2.csv', index=False)
# print(df)
# print(df.columns)
# df.to_csv('test2.csv', index=False)

df[df.columns] = df[df.columns].replace({'\r', ' '}, regex=True)

df.rename(columns={'1': 'Centre'}, inplace=True)

df = df[~df.Centre.str.contains('Table', na=False)]

df['State'] = df['Centre'].apply(lambda x: x.split(':')[1].strip() if type(x) is str and 'State' in x else np.nan)
df['District'] = df['Centre'].apply(lambda x: x.split(':')[1].strip() if type(x) is str and 'District' in x else np.nan)

df.State.ffill(inplace=True)
df.District.ffill(inplace=True)

df = df[~df.Centre.str.contains('State', na=False)]
df = df[~df.Centre.str.contains('District', na=False)]

df['Centre'] = df['Centre'].apply(lambda x: x if len(x) > 0 else np.nan)

df.Centre.ffill(inplace=True)

df.mask(df == np.nan, None).Centre.ffill(inplace=True)

df['Labour Category'] = df['Labour Category'].apply(lambda x: x if len(x) > 0 else np.nan)
df['Labour Type'] = df['Labour Type'].apply(lambda x: x if len(x) > 0 else np.nan)

df['Labour Category'].ffill(inplace=True)
df['Labour Type'].ffill(inplace=True)

# print(df.columns)
# print(type(df))
# df.columns = ['Centre', 'Labour Category', 'Labour Type', 'Gender', 'July', 'August', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Annual Average', 'State', 'District']

(df.to_csv('test1.csv', index=False))

# from ctypes.util import find_library
# print(find_library("gs"))





