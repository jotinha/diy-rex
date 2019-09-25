from scipy.sparse import spmatrix
from typing import Iterator, Tuple

from diyrex.algo import similarity, get_items_from_user


def recommend_user_user_cf(i : int, R : spmatrix, min_score = 0.9) -> Iterator[Tuple[int, float]]:
    "recommend_user_user_cf products from similar users that the user never saw"

    for j in range(R.shape[0]):
        if similarity(R[i], R[j]) > min_score:
            for product in get_items_from_user(j, R):
                if product not in get_items_from_user(i, R):
                    yield product, R[j,product]


def related(k : int, R : spmatrix, min_score = 0.9) -> Iterator[Tuple[int,float]]:
    "show related products based on co-occurency"

    for l in range(R.shape[1]):
        score = similarity(R[:,k], R[:,l])
        if score > min_score:
            yield l, score


def recommend_item_item_cf(i : int, R : spmatrix, min_score = 0.9) -> Iterator[Tuple[int, float]]:
    "Recommend things liked by people who rate highly the same things as you"

    for product in get_items_from_user(i, R):
        for other_product, related_score in related(product, R):
            yield other_product, related_score


