from diyrex.data import load, stats
from diyrex.ratings import compute_implicit_ratings

signals = load('data/listenbrainz/parsed/sample.csv')

ratings = compute_implicit_ratings(signals)

print("\nsignals:")
stats(signals)
print(signals)

print("\nratings:")
stats(ratings)
print(ratings)