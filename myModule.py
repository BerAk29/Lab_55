import pandas as pd

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)
"""
df = pd.DataFrame([[10, 20, 30], [40, 50, 60]])
ser = pd.Series([70, 80, 90], name='new row')
print('{}\n'.format(df))

df2 = df.append(ser)
print('{}\n'.format(df2))

df3 = df.append(ser, ignore_index = True)
print('{}\n'.format(df3))

df3 = pd.DataFrame([[100, 110, 120],[120, 120, 130]])
df4 = df.append(df3)
print('{}\n'.format(df4))
"""