from diyrex.data import load, stats
from diyrex import ratings
from diyrex.matrix import table_to_sparse_matrix

signals = load('data/listenbrainz/parsed/sample.csv')

print("\nsignals:")
stats(signals)
print(signals)
print(signals.dtypes)

ratings = ratings.compute_implicit_ratings_3(signals)
print("\nratings:")
stats(ratings)
print(ratings)

R = table_to_sparse_matrix(ratings)
print(R)

#do some checks
user, item, rating = ratings.iloc[0]
i = R.rows.index(user)
j = R.cols.index(item)

assert R.matrix[i,j] == rating

#recommend
from diyrex.algo.popular import most_highly_rated, most_popular

print("\n# Most highly rated:")
print('\n'.join(most_highly_rated(ratings,10)))

print("\n# Most popular:")
print('\n'.join(most_popular(ratings,10)))
