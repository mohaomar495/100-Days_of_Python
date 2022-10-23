#here are game images don't change.
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

import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, 2)
if user_choice >= 3 or computer_choice < 0:
  print("you choose an invalid number, you lose!")
else:
  print(game_images[user_choice])
  print("computer choice:")
  print(game_images[computer_choice])
  
  if user_choice == 0 and computer_choice == 2:
    print("you win!")
  elif user_choice == 2 and computer_choice == 0:
    print("you lose!")
  elif computer_choice == 1 and user_choice == 0:
    print("you lose!")
  elif computer_choice == 0 and user_choice == 1:
    print("you win!")
  elif computer_choice == 2 and user_choice == 1:
    print("you lose!")
  elif computer_choice == 1 and user_choice == 2:
    print("you win!")
  else:
    print("draw!")
