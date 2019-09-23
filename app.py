from dyirex.data import load, stats

df = load('data/listenbrainz/parsed/sample.csv')

stats(df)