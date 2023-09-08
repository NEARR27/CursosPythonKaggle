import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

result = reviews[pd.isnull(reviews.country)]
print(result)

reviews['region_2'].fillna("Unknown", inplace=True)
print(reviews['region_2'])

reviews['taster_twitter_handle'] = reviews['taster_twitter_handle'].replace("@kerinokeefe", "@kerino")
print(reviews['taster_twitter_handle'])
