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

data = []
for item in items:
    for feature in np.random.choice(features, 10):
        data.append((item,feature,1.0))

content = pd.DataFrame(data,columns=['item','feature','value'])
content.to_csv('content.csv',index=False)
