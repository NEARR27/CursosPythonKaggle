import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

reviews.rename(columns={'points': 'score'}, inplace=True)
print(reviews.head())

reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}, inplace=True)
print(reviews)

reviews2 = reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
print(reviews2)
