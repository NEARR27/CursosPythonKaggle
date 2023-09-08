import pandas as pd


# Cargar el conjunto de datos
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# Realizar la agrupación por la columna 'points' y contar los registros en cada grupo
points_count = reviews.groupby('points').points.count()
print(points_count)


min_price_by_points = reviews.groupby('points').price.min()
print(min_price_by_points)

winery_first_title = reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
print(winery_first_title)

max_points_reviews = reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df['points'].idxmax()])
print(max_points_reviews)

country_price_stats = reviews.groupby(['country'])['price'].agg([len, min, max])
print(country_price_stats)

