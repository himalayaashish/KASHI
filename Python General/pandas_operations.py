import pandas as pd
import numpy as np
df = pd.read_csv('data.csv')

print(df)

print(df.shape[0])
print(df[['total_bill', 'tip', 'smoker', 'time']].head(5))

print(df.assign(tip_rate=df['tip'] / df['total_bill']).head(5))

print(df[df['time'] == 'Dinner'].head(5))
# or
"""
is_dinner = df['time'] == 'Dinner'
print(df[is_dinner].head(5))
"""
print(df[(df['time'] == 'Dinner') & (df['tip'] > 5.00)])
print(df[(df['size'] >= 5) | (df['total_bill'] > 50)])

# Null Check
df2 = pd.DataFrame({'col1': ['A', 'B', np.NaN, 'C', 'D'],'col2': ['F', np.NaN, 'G', 'H', 'I']})
print(df2)

print(df2[df2['col2'].isna()])
print(df.groupby('sex').size())
print(df.groupby('sex').count())

# how tip amount differs by day
print(df.groupby('day').agg({'tip': np.mean, 'day': np.size}))

print(df.groupby(['smoker', 'day']).agg({'tip': [np.size, np.mean]}))

#inner join
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],'value': np.random.randn(4)})
df2 = pd.DataFrame({'key': ['B', 'D', 'D', 'E'],'value': np.random.randn(4)})
print(pd.merge(df1, df2, on='key'))


print(pd.merge(df1, df2, on='key', how='left'))

print(pd.merge(df1, df2, on='key', how='right'))

print(pd.merge(df1, df2, on='key', how='outer'))

print(pd.concat([df1, df2]))

print(pd.concat([df1, df2]).drop_duplicates())

print(df.nlargest(10 + 5, columns='tip').tail(10))
















