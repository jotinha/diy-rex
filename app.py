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

R = table_to_sparse_matrix(ratings)
print(R)

# %%

#do some checks
user, item, rating = ratings.iloc[0]
i = R.rows.index(user)
j = R.cols.index(item)

assert R.matrix[i,j] == rating


# %%
"""
## Most popular
"""

from diyrex.algo.popular import most_highly_rated, most_popular

print("\n* Most highly rated:")
print('\n'.join(most_highly_rated(ratings,10)))

print("\n* Most popular:")
print('\n'.join(most_popular(ratings,10)))
