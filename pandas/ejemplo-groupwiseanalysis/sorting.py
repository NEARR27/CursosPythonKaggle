import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])

# Restablecer el índice
countries_reviewed = countries_reviewed.reset_index()
# Ordenar el DataFrame por la columna 'len' (cantidad de descripciones)
countries_reviewed_sorted = countries_reviewed.sort_values(by='len')
# Mostrar el DataFrame ordenado
print(countries_reviewed_sorted)

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
# Restablecer el índice
countries_reviewed = countries_reviewed.reset_index()
# Ordenar el DataFrame por la columna 'len' (cantidad de descripciones) en orden descendente
countries_reviewed_sorted = countries_reviewed.sort_values(by='len', ascending=False)
# Mostrar el DataFrame ordenado
print(countries_reviewed_sorted)

# Agrupar por 'country' y 'province' y contar la cantidad de descripciones en cada grupo
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
# Restablecer el índice
countries_reviewed = countries_reviewed.reset_index()
# Ordenar el DataFrame por el índice
countries_reviewed_sorted = countries_reviewed.sort_index()
# Mostrar el DataFrame ordenado
print(countries_reviewed_sorted)

# Agrupar por 'country' y 'province' y contar la cantidad de descripciones en cada grupo
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
# Restablecer el índice
countries_reviewed = countries_reviewed.reset_index()
# Ordenar el DataFrame primero por 'country' y luego por 'len'
countries_reviewed_sorted = countries_reviewed.sort_values(by=['country', 'len'])
# Mostrar el DataFrame ordenado
print(countries_reviewed_sorted)

