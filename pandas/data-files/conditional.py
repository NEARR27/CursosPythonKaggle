import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

italian_wines = reviews[reviews.country == 'Italy']
print(italian_wines)

italian_wines = reviews.loc[reviews.country == 'Italy']
print(italian_wines)

italian_high_quality_wines = reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
print(italian_high_quality_wines)

italian2 = reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]
print(italian2)

italy = reviews.loc[reviews.country.isin(['Italy', 'France'])]
print(italy)

italy1 = reviews.loc[reviews.price.notnull()]
print(italy1)

