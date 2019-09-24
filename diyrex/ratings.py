import pandas

def compute_implicit_ratings(signals : pandas.DataFrame):
    ratings = signals.groupby([signals.user, signals.item]).apply(lambda g: 1)
    return ratings.reset_index()


