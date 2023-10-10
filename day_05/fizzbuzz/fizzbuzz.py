num_entered = False

while not num_entered:
  target = input('Enter a number: ')

  try:
    target = int(target)
    num_entered = True
  except:
    print('Please enter a valid integer.')

for i in range(1, target + 1):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  elif i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)
