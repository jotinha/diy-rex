import dask.dataframe as dd
import pandas as pd

DATE_COL = 'listened_at'
USER_COL = 'user_name'
ITEM_COL = 'artist_name'

ddf = dd.read_csv('../raw/*.csv', dtype='str')

ddf = ddf[[DATE_COL, USER_COL, ITEM_COL]]

ddf = ddf.rename(columns={DATE_COL: 'date', USER_COL: 'user', ITEM_COL: 'item'})

df: pd.DataFrame = ddf.compute()

user_count : pd.Series = df.user.value_counts(ascending=True)
item_count : pd.Series = df.item.value_counts(ascending=True)

sample_users = user_count[user_count.between(10,100)].index.tolist()
len(sample_users)

decent_users = user_count[user_count.between(10,1000)].index.tolist()
decent_items = item_count[item_count >= 5].index.tolist()

df = df[df.user.isin(decent_users) * df.item.isin(decent_items)]

print(len(df),'lines')
df.to_csv('data.csv',index=False)