import random

names = "Barney, Chloe, James, Kat"
names = names.split(", ")

chosen_name = names[random.randint(0, len(names) - 1)]

print(f"{chosen_name} is going to pay for lunch today")
