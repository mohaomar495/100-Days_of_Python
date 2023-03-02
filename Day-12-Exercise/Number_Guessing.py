import random

chosen = random.randint(1, 101)
print(chosen)

print("Welcome the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("choose a difficulty. Type 'easy' or 'hard': ").lower()

def hard_mode():
  attempts = 5
  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < chosen:
      print("Too low")
      
    elif guess > chosen:
      print("Too high")

    elif guess == chosen:
      print(f"You got it!, the answer was {chosen}")
      break
    attempts -= 1
    print("Guess Again")
  if attempts == 0:
    if guess != chosen:
        print("you've run out of guesses, you lose")

def easy_mode():
  attempts = 10
  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < chosen:
      print("Too low")
      print("Guess Again")
    elif guess > chosen:
      print("Too high")
      print("Guess Again")
    elif guess == chosen:
      print(f"You got it!, the answer was {chosen}")
      break
    attempts -= 1
  if attempts == 0:
    if guess != chosen:
        print("you've run out of guesses, you lose")

if difficulty == "easy":
  easy_mode()
elif difficulty == "hard":
  hard_mode()