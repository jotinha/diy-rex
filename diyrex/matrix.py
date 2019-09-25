import pandas
from scipy import sparse as sp
from typing import List


def table_to_sparse_matrix(ratings: pandas.DataFrame, x : str, y : str, v: str) -> (sp.spmatrix, List, List):
    assert ratings[x].dtype == 'category' and ratings[y].dtype == 'category'

    i = ratings[x].cat.codes
    j = ratings[y].cat.codes
    data = ratings[v].values

    users = ratings[x].cat.categories.values
    items = ratings[y].cat.categories.values

    mat = sp.coo_matrix((data, (i, j)), dtype='float32')
    mat = mat.tocsr()
    return mat, list(users), list(items)

