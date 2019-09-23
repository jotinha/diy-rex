from typing import Iterator

from diyrex.algo import similarity, get_products_from_user

def recommend(user, users) -> Iterator:
    "recommend products from similar users that the user never saw"
    for other_user in users:
        if similarity(user, other_user) > 0.9:
            for product in get_products_from_user(other_user):
                if product not in get_products_from_user(user):
                    yield product

