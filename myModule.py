import pandas as pd
"""
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
# print(df)


df = pd.DataFrame([[10, 20, 30], [40, 50, 60]])
ser = pd.Series([70, 80, 90], name='new row')
print("*\n"'{}\n'.format(df))

df2 = df.append(ser)
print("**\n"'{}\n'.format(df2))

df3 = df.append(ser, ignore_index = True)
print("***\n"'{}\n'.format(df3))

df3 = pd.DataFrame([[100, 110, 120],[120, 120, 130]])
df4 = df.append(df3)
print("****\n"'{}\n'.format(df4))
"""


data = {'Name':['Bertrand', 'Paul', 'Christian', 'Parfait'],
        'Age':[27, 24, 22, 32],
        'Address':['France', 'UK', 'USA', 'Morocco'],
        'Qualification':['Msc', 'MBA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df)
print('\n', df[['Name', 'Qualification']])


from contextlib import redirect_stdout

with open('help_out3.txt', 'w') as f:
    with redirect_stdout(f):
        help(pd.DataFrame)

