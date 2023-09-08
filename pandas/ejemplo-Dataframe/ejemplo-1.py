import pandas as pd

dataframe1= pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(dataframe1)

dataframe2 = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(dataframe2)

dataframe3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print(dataframe3)
