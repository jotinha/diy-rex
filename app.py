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
user, item, rating = ratings.iloc[0]
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

from diyrex.algo.collaborative_user_user import recommend

print(f"\n* Recs form user {users[i]}")
for k, r in islice(recommend(i, R), 10):
    print(items[k], r)
