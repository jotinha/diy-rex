import dask.dataframe as dd

DATE_COL = 'listened_at'
USER_COL = 'user_name'
ITEM_COL = 'artist_name'

ddf = dd.read_csv('../raw/*.csv',dtype='str')

ddf = ddf[[DATE_COL, USER_COL, ITEM_COL]]

# ddf = ddf.astype({
#     DATE_COL: 'M8[us]',
#     USER_COL: 'category',
#     ITEM_COL: 'category'
# })

ddf = ddf.rename(columns={DATE_COL:'date', USER_COL: 'user', ITEM_COL: 'item'})

ddf.sample(frac=0.0001).compute().to_csv('sample.csv', index=False)

ddf.compute().to_csv('data.csv',index=False)


