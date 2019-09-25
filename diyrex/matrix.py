import pandas
from scipy import sparse as sp
from typing import List


def table_to_sparse_matrix(ratings: pandas.DataFrame) -> (sp.spmatrix, List, List):
    assert ratings['user'].dtype == 'category' and ratings['item'].dtype == 'category'

    i = ratings['user'].cat.codes
    j = ratings['item'].cat.codes
    data = ratings['rating'].values

    users = ratings['user'].cat.categories.values
    items = ratings['item'].cat.categories.values

    mat = sp.coo_matrix((data, (i, j)), dtype='float32')
    mat = mat.tocsr()
    return mat, list(users), list(items)

