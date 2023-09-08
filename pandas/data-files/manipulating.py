import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

reviews = reviews.set_index("title")
print(reviews.head())

