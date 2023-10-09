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

print()

# We can update the index on creation of the dataframe if we want to
purchases = pd.DataFrame(data, index=['Barney', 'Chloe', 'James', 'Kat'])
print(purchases)

print()

# We can access an individual customers purchase using the .loc pandas method
print(purchases.loc['Barney'])
