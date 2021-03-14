
import numpy as np

import tabula

import pandas as pd

file = "AgriWages2015-16.pdf"

# df = tabula.read_pdf(file, pages=[34], multiple_tables=True)

import camelot

year = [15, 16]

df_final = pd.DataFrame(columns=['Centre', 'Gender', 'Labour Category', 'Labour Type', f'July-{year[0]}', f'August-{year[0]}', f'September-{year[0]}', f'October-{year[0]}', f'November-{year[0]}', f'December-{year[0]}', f'January-{year[1]}', f'February-{year[1]}', f'March-{year[1]}', f'April-{year[1]}', f'May-{year[1]}', f'June-{year[1]}', 'Annual Average', 'State', 'District'])

for i in range(17, 221):
       print(f"Processing page number: {i}")
       pages = str(i)

       # for i in range(33, 251):
       #        pages += str(i) + ','

       # pages = pages[:-1]

       tables = camelot.read_pdf(file, pages=pages)

       # print(tables[0].df)
       # import matplotlib.pyplot as plt
       # camelot.plot(tables[0], kind='grid').show()
       # plt.show()

       df = pd.DataFrame(tables[0].df)
       df.columns = df.iloc[0]
       df = df[1:]

       df = df[['', 'Labour \nCategory', 'Labour \nType', 'July', 'August',
              'September', 'October', 'November', 'December', 'January', 'February',
              'March', 'April', 'May', 'June', 'Annual \nAverage']]

       # print(df.columns)
       df.columns = ['1', 'Gender', 'Labour Category', 'Labour Type', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June', 'Annual Average']
       df.dropna(inplace=True)
       # df.to_csv('tes2.csv', index=False)
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
       df = df[~df.Centre.str.contains('District', na=False) & df.index != len(df)]

       df['Centre'] = df['Centre'].apply(lambda x: x if len(x) > 0 else np.nan)

       df.Centre.ffill(inplace=True)

       df.mask(df == np.nan, None).Centre.ffill(inplace=True)

       df['Labour Category'] = df['Labour Category'].apply(lambda x: x if len(x) > 0 else np.nan)
       df['Labour Type'] = df['Labour Type'].apply(lambda x: x if len(x) > 0 else np.nan)

       # print(df.columns)
       # print(type(df))
       df.columns = ['Centre', 'Gender', 'Labour Category', 'Labour Type', f'July-{year[0]}', f'August-{year[0]}', f'September-{year[0]}', f'October-{year[0]}', f'November-{year[0]}', f'December-{year[0]}', f'January-{year[1]}', f'February-{year[1]}', f'March-{year[1]}', f'April-{year[1]}', f'May-{year[1]}', f'June-{year[1]}', 'Annual Average', 'State', 'District']

       df_final = pd.concat([df_final, df])

df_final['State'].ffill(inplace=True)
df_final['District'].ffill(inplace=True)
df_final = df_final[~df_final.Centre.str.contains("District")]

df_final['Centre'] = df_final['Centre'].apply(lambda x: x.split(':')[1].strip())
df_final['Centre_length'] = df_final['Centre'].apply(lambda x: len(x))
# df_final = df_final[df_final['Centre_length'] < 12]

df_final['Labour Category'].ffill(inplace=True)
df_final['Labour Type'].ffill(inplace=True)

df_final_long_centre_names = df_final[df_final['Centre_length'] >= 12]

(df_final.to_csv(f'20{year[0]}_{year[1]}.csv', index=False))
df_final_long_centre_names.to_csv('test3.csv', index=False)
# print(df_final)
# from ctypes.util import find_library
# print(find_library("gs"))





