sorted_varieties = reviews.groupby('variety').price.agg([min,max]).sort_values(by=['min', 'max'], ascending=False)

# Check your answer
q4.check()
sorted_varieties
