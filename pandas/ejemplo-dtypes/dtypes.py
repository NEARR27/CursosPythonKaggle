import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

print(reviews['price'].dtype)

print(reviews.dtypes)

new_points = reviews['points'].astype('float64')
print(new_points)

print(reviews.index.dtype)
