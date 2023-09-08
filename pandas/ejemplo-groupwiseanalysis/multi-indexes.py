import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
mi = countries_reviewed.index
print(type(mi))

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed_reset = countries_reviewed.reset_index()
print(countries_reviewed_reset)
