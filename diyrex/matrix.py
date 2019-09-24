import pandas
from dataclasses import dataclass
from scipy import sparse as sp
from typing import List


@dataclass
class DIYMatrix:
    rows: List
    cols: List
    matrix: sp.spmatrix
    name: str = 'matrix'

    def __repr__(self):
        return self.name + ': ' + repr(self.matrix)


def table_to_sparse_matrix(ratings: pandas.DataFrame) -> DIYMatrix:
    assert ratings['user'].dtype == 'category' and ratings['item'].dtype == 'category'

    i = ratings['user'].cat.codes
    j = ratings['item'].cat.codes
    data = ratings['rating'].values

    users = ratings['user'].cat.categories.values
    items = ratings['item'].cat.categories.values

    mat = sp.coo_matrix((data, (i, j)))
    mat = mat.tocsc()
    return DIYMatrix(rows=list(users), cols=list(items), matrix=mat, name='R')
