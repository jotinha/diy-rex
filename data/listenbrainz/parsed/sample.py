import pandas as pd

DATE_COL = 'listened_at'
USER_COL = 'user_name'
ITEM_COL = 'artist_name'

df = pd.read_csv('data.csv')

user_count : pd.Series = df.groupby('user')['item'].nunique()
sample_users = user_count.sample(100).index.tolist()

df_sample = df[df.user.isin(sample_users)]
item_count: pd.Series = df_sample.groupby('item')['user'].nunique()

sample_items = item_count[item_count > 5].index.tolist()

df_sample_2 = df[df.user.isin(sample_users) * df.item.isin(sample_items)]

print(len(df_sample_2), 'lines')

df_sample_2.to_csv('sample.csv', index=False)