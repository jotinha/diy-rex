from scipy.sparse import spmatrix
from typing import Iterator, Tuple

from diyrex.algo import similarity, get_items_from_user


def recommend(i : int, R : spmatrix, min_score = 0.9) -> Iterator[Tuple[int,float]]:
    "recommend products from similar users that the user never saw"

    for j in range(R.shape[0]):
        if similarity(R[i], R[j]) > min_score:
            for product in get_items_from_user(j, R):
                if product not in get_items_from_user(i, R):
                    yield product, R[j,product]

