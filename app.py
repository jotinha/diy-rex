from itertools import islice

import numpy as np
import pandas as pd

from diyrex.data import load, stats
from diyrex import ratings
from diyrex.matrix import table_to_sparse_matrix

np.random.seed(123)


# %%
"""
## Load signals
"""
signals = load('data/listenbrainz/parsed/data.csv', ['date','user','item'])

print("\nsignals:")
stats(signals)
signals

# %%
"""
## Convert to ratings
"""

ratings = ratings.compute_implicit_ratings_3(signals)
print("\nratings:")
stats(ratings)
ratings

# %%
"""
## Convert to matrix
"""

R, users, items = table_to_sparse_matrix(ratings, 'user', 'item', 'rating')
R

# %%

#do some checks
user, item, rating = ratings.sample(1).iloc[0]
i = users.index(user)
j = items.index(item)

assert R[i,j] == np.float32(rating)


# %%
"""
## Most popular
"""

from diyrex.algo.popular import most_highly_rated, most_popular

print("\n* Most highly rated:")
print('\n'.join(most_highly_rated(ratings,10)))

print("\n* Most popular:")
print('\n'.join(most_popular(ratings,10)))

# %%
"""
## User-user collaborative filtering
"""

from diyrex.algo.collaborative import recommend_user_user_cf

print(f"\n* Recs for user {users[i]}")
for k, r in islice(recommend_user_user_cf(i, R), 10):
    print(items[k], r)

# %%
"""
## Related items
"""
from diyrex.algo.collaborative import related
print(f"\n* Items related to: {items[j]}")
for k, r in islice(related(j, R), 10):
    print(items[k], r)


# %%
"""
## Item-item collaborative filtering
"""

from diyrex.algo.collaborative import recommend_item_item_cf
print(f"\n* Recs for user: {users[i]}")
for k, r in islice(recommend_item_item_cf(i, R), 10):
    print(items[k], r)

# %%
"""
## Efficient item-item collaborative filtering
"""

from diyrex.algo.efficient import self_similarity_matrix, recommend_with_S

S = self_similarity_matrix(R.T)
print(f"\n* Recs for user: {users[i]}")
for k,r in recommend_with_S(i, R, S):
    print(items[k], r)

# %%
"""
## Content based
"""

content = load('data/listenbrainz/parsed/content.csv',  ['item','feature','value'])

# item category codes must be the same so the matrices are aligned
content['item'].cat.reorder_categories(items, inplace=True)

assert all(content.item.cat.categories == signals.item.cat.categories)

I,items2,features = table_to_sparse_matrix(content, 'item', 'feature', 'value')

assert items == items2

from diyrex.algo.content import similar, recommend_content_based

print(f"\n* Similar to item: {items[j]}")
for k, r in islice(similar(i, I), 10):
    print(items[k], r)

print(f"\n* Recs for user: {users[i]}")
for k, r in islice(recommend_content_based(i, R), 10):
    print(items[k], r)
