import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

selection = [rock, paper, scissors]

print('Welcome to rock, paper, scissors!')
player_choice = input('What do you choose? Type 1 for rock, 2 for paper or 3 for scissors.\n')
player_choice = int(player_choice) - 1
computer_choice = random.randint(0, 2)

winner = ''

if(player_choice == computer_choice):
  result = "It's a draw."
elif(player_choice == 0 and computer_choice == 2 
     or player_choice == 1 and computer_choice == 0
     or player_choice == 2 and computer_choice == 1):
  result = 'You win!'
else:
  result = 'You lose.'

print(f'{selection[player_choice]}\n')
print(f"Computer chose:\n {selection[computer_choice]}\n")
print(result)
