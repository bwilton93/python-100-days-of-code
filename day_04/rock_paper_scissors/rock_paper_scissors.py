import random, selection

choice_made = False

print('Welcome to rock, paper, scissors!')

while(not choice_made):
  player_choice = input('What do you choose? Type 1 for rock, 2 for paper or 3 for scissors.\n')
  if(player_choice != '0' and player_choice != '1' and player_choice != '2'):
    print('That is not a valid input, try again.')
  else:
    choice_made = True

player_choice = int(player_choice) - 1
computer_choice = random.randint(0, 2)

if(player_choice == computer_choice):
  result = "It's a draw."
elif(player_choice == 0 and computer_choice == 2 
     or player_choice == 1 and computer_choice == 0
     or player_choice == 2 and computer_choice == 1):
  result = 'You win!'
else:
  result = 'You lose.'

print(f'{selection.selection[player_choice]}\n')
print(f"Computer chose:\n {selection.selection[computer_choice]}\n")
print(result)
