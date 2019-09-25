"""
Fake some content based data
"""

import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

items = df.item.unique()
n_items = len(items)
n_feats = 100
features = ['f' + str(i) for i in range(n_feats)]

with open('content.csv','wt') as f:
    print("item","feature",sep=',', file=f)
    for item in items:
        for feature in features:
            if np.random.random() < 0.01:
                print(item, feature, sep=',', file=f)