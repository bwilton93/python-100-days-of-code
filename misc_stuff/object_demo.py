from person import Person

list_of_people = []

barney = Person('Barney', 30)
list_of_people.append(barney)

chloe = Person('Chloe', 24)
list_of_people.append(chloe)

# We can call object defined functions on individual objects
barney.formatted_output()

# We can also loop through the array and call an object defined function on each item
for person in list_of_people:
  person.formatted_output()

# We can access individual properties of an object
print(f'Users name is: {barney.name}')
print(f'Users age is: {barney.age}')

# What happens if we want to update a value now?
print(f'Chloe is: {chloe.age}')
chloe.age += 1
print(f'After another rotation around the sun, Chloe is now: {chloe.age}')
