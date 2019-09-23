from diyrex.algo import similarity, get_products_from_user


def related(product, products):
    "show related products based on co-occurency"
    for other_product in products:
        if similarity(product, other_product) > 0.9:
            yield other_product

def recommend(user, products):
    "Recommend things liked by people who rate highly the same things as you"

    for product in get_products_from_user(user):
        for other_product in related(product, products):
            yield other_product






