from itertools import islice

from typing import Iterator


def preview(recs : Iterator, keys, n=10, title= None):
    hr = lambda : print('-' * 30)

    hr()
    if title:
        print(title)
        hr()

    for k in islice(recs,n):
        print(keys[k])
    print()