from itertools import islice

import numpy as np
import pandas as pd

from diyrex.algo import get_items_from_user
from diyrex.data import load, stats
from diyrex import ratings, preview
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
user, item, rating = ratings[ratings.item=='Metallica'].sample(1).iloc[0]
i = users.index(user)
j = items.index(item)

assert items[j] == "Metallica"

assert R[i,j] == np.float32(rating)

preview(get_items_from_user(i, R), items, n=10, title=f"Top rated items for '{users[i]}'")


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

preview(recommend_user_user_cf(i, R), items, title=f"User-User CF for '{users[i]}'")

# %%
"""
## Related items
"""
from diyrex.algo.collaborative import related

preview(related(j, R), items, title=f"Items related to '{items[j]}'")


# %%
"""
## Item-item collaborative filtering
"""

from diyrex.algo.collaborative import recommend_item_item_cf

preview(recommend_item_item_cf(i, R), items, title=f"Item-Item CF for user '{users[i]}'")

# %%
"""
## Content based
"""

content = load('data/listenbrainz/parsed/content.csv',  ['item','feature','value'])

# item category codes must be the same so the matrices are aligned
content['item'].cat.reorder_categories(items, inplace=True)

assert all(content.item.cat.categories == signals.item.cat.categories)

I,features, items2 = table_to_sparse_matrix(content, 'feature', 'item', 'value')

assert items == items2

from diyrex.algo.content import similar, recommend_content_based

preview(similar(i,I),items,title=f"Similar to item: {items[j]}")
preview(recommend_content_based(i,R, S),items,title=f"Content-based recs for user: {users[i]}")

# %%
"""
## Efficient item-item collaborative filtering
"""

from diyrex.algo.efficient import self_similarity_matrix, recommend_with_S

S = self_similarity_matrix(R.T)
preview(recommend_with_S(i, R, S), items, title=f"Efficient Item-Item CF for user '{users[i]}'")
