from itertools import islice

from diyrex.data import load, stats
from diyrex import ratings
from diyrex.matrix import table_to_sparse_matrix

# %%
"""
## Load signals
"""
signals = load('data/listenbrainz/parsed/sample.csv')

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

R, users, items = table_to_sparse_matrix(ratings)
R

# %%

#do some checks
user, item, rating = ratings.sample(1).iloc[0]
i = users.index(user)
j = items.index(item)

assert R[i,j] == rating


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
