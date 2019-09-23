import pandas

def compute_implicit_ratings(df : pandas.DataFrame):
    ratings = df.groupby([df.user, df.item]).apply(lambda g: 1)
    return ratings.reset_index()


