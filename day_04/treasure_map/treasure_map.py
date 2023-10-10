line1 = [" ", "️ ", "️ "]
line2 = [" ", " ", "️ "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?

# CLUMSY METHOD
# x_coordinate = int(position[1]) - 1
# y_coordinate = position[0].lower()

# if y_coordinate == 'a':
#   y_coordinate = 0
# elif y_coordinate == 'b':
#   y_coordinate = 1
# elif y_coordinate == 'c':
#   y_coordinate = 2
# else:
#   print('Y coordinate not valid')

# map[x_coordinate][y_coordinate] = 'X'

# BETTER METHOD
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)  # returns index position of letter co-ordinate

number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
