from typing import Iterator

from diyrex.matrix import Vector

class User(Vector):
    pass

class Product(Vector):
    pass

def similarity(user1 : User, user2 : User) -> float:
    return user1.matrix * user2.matrix.T

def get_products_from_user(user : User, R) -> Iterator:
    raise NotImplementedError