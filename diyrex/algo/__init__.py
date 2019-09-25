import numpy as np

from scipy.sparse import spmatrix, csr_matrix
from scipy.spatial.distance import cosine
from typing import List


def similarity(v1: spmatrix, v2: spmatrix) -> float:
    """
        >>> R = csr_matrix([[1,0,1],[1,1,0]])
        >>> similarity(R[0],R[1])
        0.5
    """
    assert v1.shape == v2.shape
    return 1 - cosine(v1.A.flatten(), v2.A.flatten())


def get_items_from_user(i: int, R: spmatrix) -> List:
    """
    >>> R = csr_matrix([[1,0,0],[0,1,0],[1,1,0]])
    >>> get_items_from_user(0, R)
    [0]
    >>> get_items_from_user(2, R)
    [0, 1]

    """
    assert isinstance(R, csr_matrix)
    scores = R[i].data
    idxs = R[i].indices
    return idxs[np.argsort(-scores)]
