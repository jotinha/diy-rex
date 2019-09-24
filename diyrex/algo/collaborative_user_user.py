from typing import Iterator

from diyrex.algo import similarity, get_products_from_user, User
from diyrex.matrix import Matrix


def recommend(user : User, R : Matrix) -> Iterator:
    "recommend products from similar users that the user never saw"


    for other_user in R.row_names:
        if similarity(user, R.get_row_vector()) > 0.9:
            for product in get_products_from_user(other_user):
                if product not in get_products_from_user(user):
                    yield product

