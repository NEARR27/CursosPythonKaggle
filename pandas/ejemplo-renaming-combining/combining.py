import pandas as pd

canadian_youtube = pd.read_csv("CAvideos.csv", index_col=0)
british_youtube = pd.read_csv("GBvideos.csv", index_col=0)

concatenated_youtube = pd.concat([canadian_youtube, british_youtube])
print(concatenated_youtube)

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
merged = left.merge(right, left_index=True, right_index=True, suffixes=('_CAN', '_UK'))
print(merged)
