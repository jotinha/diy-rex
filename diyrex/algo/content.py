from collections import Iterator

from _ast import Tuple
from scipy.sparse import spmatrix

from diyrex.algo.collaborative import related


def similar(k : int, I : spmatrix, min_score = 0.9) -> Iterator[Tuple[int,float]]:
    "return similar items based on their content matrix"

    yield from related(k, I, min_score = min_score)
