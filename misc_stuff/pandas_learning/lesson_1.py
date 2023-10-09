import pandas as pd

# Organised data for apples and oranges
# Each type of fruit is considered a series
# The whole set of data can be combined into a dataframe
data = {
  'apples': [3, 2, 0, 1], 
  'oranges': [0, 3, 7, 2] 
}

# Pass this data to the pandas dataframe constructor
purchases = pd.DataFrame(data)
print(purchases)

print() # Empty line to seperate the two dataframes for readability

# We can update the index on creation of the dataframe if we want to
purchases = pd.DataFrame(data, index=['Barney', 'Chloe', 'James', 'Kat'])
print(purchases)
