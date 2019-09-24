import pandas
from diyrex.data import load, stats
from diyrex import ratings

signals = load('data/listenbrainz/parsed/sample.csv')

print("\nsignals:")
stats(signals)
print(signals)
print(signals.dtypes)


ratings = ratings.compute_implicit_ratings_3(signals)
print("\nratings:")
stats(ratings)
print(ratings)