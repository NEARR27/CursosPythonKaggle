import pandas as pd

# Cargar el conjunto de datos
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# Mostrar la descripción de la columna "points"
print(reviews['points'].describe())

# Mostrar la descripción de la columna "taster_name"
print(reviews['taster_name'].describe())

# Calcular la media de la columna "points"
print(reviews['points'].mean())

# Mostrar los valores únicos en la columna "taster_name"
print(reviews['taster_name'].unique())

# Contar cuántas veces aparece cada valor en la columna "taster_name"
print(reviews['taster_name'].value_counts())




