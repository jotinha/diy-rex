from scipy.sparse import spmatrix
from typing import Iterator

from diyrex.algo import get_items_from_user
from diyrex.algo.collaborative import related


def similar(k: int, I: spmatrix, min_score=0.9) -> Iterator[int]:
    "return similar items based on their content matrix"

    yield from related(k, I, min_score=min_score)


def recommend_content_based(i: int, R: spmatrix, I: spmatrix, min_score=0.9) -> Iterator[int]:
    "Recommend things similar to my profile"

    for product in get_items_from_user(i, R):
        for other_product, related_score in similar(product, I, min_score=min_score):
            yield other_product, related_score
