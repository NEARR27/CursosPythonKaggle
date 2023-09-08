import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

reviews['critic'] = 'everyone'
print(reviews['critic'])

reviews['index_backwards'] = range(len(reviews), 0, -1)
print(reviews['index_backwards'])
