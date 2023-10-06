line1 = [" ","️ ","️ "]
line2 = [" "," ","️ "]
line3 = [" "," "," "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

x_coordinate = int(position[1]) - 1
y_coordinate = position[0]

if y_coordinate == 'A':
  y_coordinate = 0
elif y_coordinate == 'B':
  y_coordinate = 1
elif y_coordinate == 'C':
  y_coordinate = 2
else:
  print('Y coordinate not valid')

map[x_coordinate][y_coordinate] = 'X'

print(f"{line1}\n{line2}\n{line3}")