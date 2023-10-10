target = int(input())  # Enter a number between 0 and 1000

output = 0

# This will sum all even numbers, must start at 0 to correctly use step value of 2
for i in range(0, target + 1, 2):
    output += i

print(output)
