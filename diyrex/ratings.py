import numpy as np
import pandas
import tqdm
from typing import Callable

from diyrex.cache import cacher

tqdm.tqdm_pandas(tqdm.tqdm)  # progress bars for groupby


def compute_implicit_ratings_func(signals: pandas.DataFrame, agg_func: Callable):
    ratings = signals.groupby(['user', 'item']).progress_apply(agg_func)

    # normalize
    ratings /= ratings.max()

    return ratings.to_frame(name='rating').reset_index()


def compute_implicit_ratings_1(signals):
    "rating is 1 if any interaction happened"
    return compute_implicit_ratings_func(signals, lambda g: 1)


def compute_implicit_ratings_2(signals: pandas.DataFrame):
    "rating is the number of days with interactions"
    return compute_implicit_ratings_func(signals, lambda g: g['date'].dt.date.nunique())


@cacher.cache
def compute_implicit_ratings(signals: pandas.DataFrame):
    "rating is an exponentially decaying function relative to a reference date"

    t_half = 15  # halflife of signal, if it happened 15 days before t0, it's 0.5

    λ = np.log(2) / t_half

    t0 = signals['date'].max()  # reference date is the last date in the dataset

    decay = lambda t: np.exp(-λ * (t - t0).days / t_half)

    # g['date'].apply(decay).max() is equiv to decay(g['date'].min())
    return compute_implicit_ratings_func(signals, lambda g: decay(g['date'].min()))
