#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random
choice = int(input("Please enter the seed code. "))
random.seed(choice)
random_number = random.randint(0, 1)

if (random_number == 1):
  print("Heads")
else:
    print("Tails")
