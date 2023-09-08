import pandas as pd

# Cargar el conjunto de datos
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# Calcular la media de los puntos y restarla de la columna "points"
review_points_mean = reviews.points.mean()
reviews['points'] = reviews.points - review_points_mean
print(reviews)

# Utilizar apply para aplicar la función remean_points a cada fila
def remean_points(row):
    row['points'] = row['points'] - review_points_mean
    return row

reviews = reviews.apply(remean_points, axis='columns')
print(reviews)

# Mostrar el primer registro
print(reviews.head(1))

# Calcular la diferencia entre "points" y la media nuevamente
review_points_mean = reviews.points.mean()
reviews['points'] = reviews.points - review_points_mean
print(reviews)

# Concatenar "country" y "region_1" en una nueva columna
reviews['country_region'] = reviews['country'] + " - " + reviews['region_1']
print(reviews)


