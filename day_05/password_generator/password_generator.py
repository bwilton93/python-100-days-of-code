import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

output = []


# Helper function for input validation
def _input(message, input_type=str):
    while True:
        try:
            return input_type(input(message))
        except:
            pass


# Function for randomising from each array
def get_random_character(input_num, array):
    for i in range(0, input_num):
        output.append(array[random.randint(0, len(array) - 1)])


print("Welcome to the PyPassword Generator!")
nr_letters = _input("How many letters would you like in your password?\n", int)
nr_symbols = _input(f"How many symbols would you like?\n", int)
nr_numbers = _input(f"How many numbers would you like?\n", int)

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
get_random_character(nr_letters, letters)
get_random_character(nr_symbols, symbols)
get_random_character(nr_numbers, numbers)

print("".join(output))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(output)
print("".join(output))
