tro = reviews.description.map(lambda desc:"tropical"in desc).sum()
fru = reviews.description.map(lambda desc : "fruity"in desc).sum()
descriptor_counts = pd.Series([tro,fru], index = ["tropical", "fruity"])

# Check your answer
q6.check()
descriptor_counts
