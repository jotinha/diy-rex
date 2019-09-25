import pandas
from typing import List


def most_highly_rated(ratings: pandas.DataFrame, n=100) -> List:
    "Recommend items with the highest average rating score"

    scores = ratings.groupby('item')['rating'].mean()

    # if you want performance, use np.argpartition
    return scores.sort_values(ascending=False).head(n).index.tolist()


def most_popular(ratings: pandas.DataFrame, n=100) -> List:
    "Recommend items with most user interactions"

    scores = ratings.groupby('item')['user'].nunique()

    return scores.sort_values(ascending=False).head(n).index.tolist()
