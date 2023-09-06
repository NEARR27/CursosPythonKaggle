import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print("Setup complete.")


#ejercicio 1
dtype = reviews.rename(columns=dict(region_1='region', region_2='locale'))

#ejercicio 2
point_strings = reviews.rename_axis('wines', axis='rows')

#ejercicio 3
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"
n_missing_prices = pd.concat([gaming_products, movie_products])

#ejercicio 4
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")
reviews_per_region = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))