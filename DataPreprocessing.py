import pandas as pd


from os import walk

import os

# f = []
# for (dirpath, dirnames, filenames) in walk(os.path.join(os.getcwd(), 'files')):
#     for file in filenames:
#         df = pd.read_csv(os.path.join(os.getcwd(), 'files', file))
#         # df.drop(columns=['Annual Average'], inplace=True)
#         df = df.melt(
#             id_vars=['Centre','Gender','Labour Category','Labour Type', 'State', 'District', 'Centre_length'],
#             var_name='Date',
#             value_name='Wage'
#         )
#         df.to_csv(os.path.join(os.getcwd(), 'files', file), index=False)


# f = []
# df_final_normal = pd.DataFrame(columns=['Centre','Gender','Labour Category','Labour Type','State','District','Centre_length','Date','Wage'])
# df_final_large = pd.DataFrame(columns=['Centre','Gender','Labour Category','Labour Type','State','District','Centre_length','Date','Wage'])
#
# for (dirpath, dirnames, filenames) in walk(os.path.join(os.getcwd(), 'files')):
#     for file in filenames:
#         df = pd.read_csv(os.path.join(os.getcwd(), 'files', file))
#         df_normal = df[~df['Centre'].str.contains("FIELD LABOUR")]
#         df_large = df[df['Centre'].str.contains("FIELD LABOUR")]
#         df_final_normal = pd.concat([df_final_normal, df_normal])
#         df_final_large = pd.concat([df_final_large, df_large])
#
#
# df_final_normal.to_csv(os.path.join(os.getcwd(), 'files', "Final_normal_combined.csv"), index=False)
# df_final_large.to_csv(os.path.join(os.getcwd(), 'files', "Final_large_combined.csv"), index=False)

# df_temp = pd.read_csv(os.path.join(os.getcwd(), 'files', 'Final_normal_combined.csv'))
#
# f = []
# total_length = 0
# for (dirpath, dirnames, filenames) in walk(os.path.join(os.getcwd(), 'files')):
#     for file in filenames:
#         print(file)
#         df = pd.read_csv(os.path.join(os.getcwd(), 'files', file))
#         # df.drop(columns=['Annual Average'], inplace=True)
#         total_length += len(df)
#         # df.to_csv(os.path.join(os.getcwd(), 'files', file), index=False)

# print(len(pd.read_csv('Final_large_combined.csv')) + len(pd.read_csv('Final_normal_combined.csv')))

# print(len(df))
# df = df[~df.Centre.str.contains('SKILLED')]
# df = df[~df.Centre.str.contains('OTHER')]
# df['Word_count'] = df['Centre'].apply(lambda centre: len(centre.split(' ')))
# # df = df[(df.Centre_length > 12) & (df.Word_count >= 2)]
# # df = df[(df.Word_count >= 2)]
# df.to_csv(os.path.join(os.getcwd(), 'files', 'Final_normal_combined.csv'), index=False)
# print(len(df))

# print(total_length, len(df_temp))


df = pd.read_csv(os.path.join(os.getcwd(), 'files', 'Final_large_combined.csv'))

df['Centre_names'] = df['Centre'].apply(lambda centre: centre.rstrip(' FIELD LABOUR'))

print(list(set(df['Centre_names'])))
