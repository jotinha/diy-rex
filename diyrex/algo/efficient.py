import numpy as np
from scipy.sparse import spmatrix
from sklearn.preprocessing import normalize


def self_similarity_matrix(mat: spmatrix) -> spmatrix:
    "fast cosine similarity calculation between all rows of `mat`"

    mat = normalize(mat, norm='l2', axis=1)

    return mat * mat.T


def recommend_with_S(i: int, R : spmatrix, S: spmatrix, n = 10):
    scores = R[i] * S

    assert scores.shape == (1,R.shape[1])

    scores = scores.A[0] #to 1-D array

    idxs = np.argsort(-scores)[:n]
    yield from zip(idxs, scores[idxs])