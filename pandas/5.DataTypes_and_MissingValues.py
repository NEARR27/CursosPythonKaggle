import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

print("Setup complete.")

#ejercicio 1:
renamed = reviews.points.dtype

#ejercicio 2:
reindexed = reviews.points.astype(str)

#ejercicio 3:
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)

#ejercicio 4:
powerlifting_combined =  reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)