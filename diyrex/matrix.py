import pandas
from dataclasses import dataclass
from scipy import sparse as sp
from typing import List

@dataclass
class Vector:
    name: str
    features : List[str]
    matrix: sp.spmatrix


@dataclass
class Matrix:
    row_names: List[str]
    col_names: List[str]
    matrix: sp.spmatrix
    name: str = 'matrix'

    def __repr__(self):
        return self.name + ': ' + repr(self.matrix)

    def get_row_index(self, name):
        return self.row_names.index(name)

    def get_col_index(self, name):
        return self.col_names.index(name)

    def get_row_vector(self, name) -> Vector:
        return Vector(name = name, features=self.col_names, matrix = self.matrix[self.get_row_index(name)])

    def get_col_vector(self, name) -> Vector:
        return Vector(name = name, features=self.row_names, matrix =self.matrix[:, self.get_col_index(name)])


def table_to_sparse_matrix(ratings: pandas.DataFrame) -> Matrix:
    assert ratings['user'].dtype == 'category' and ratings['item'].dtype == 'category'

    i = ratings['user'].cat.codes
    j = ratings['item'].cat.codes
    data = ratings['rating'].values

    users = ratings['user'].cat.categories.values
    items = ratings['item'].cat.categories.values

    mat = sp.coo_matrix((data, (i, j)))
    mat = mat.tocsc()
    return Matrix(rows=list(users), cols=list(items), matrix=mat, name='R')
