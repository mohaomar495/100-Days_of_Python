#Importing some Modules to work with my project.
import random
from Hangman_logo import logo
from Hangman_pic import stages
from Hangman_word_list import word_list

print(logo)

# Randomly choosing a word from the word_list
computer_choice = random.choice(word_list)

#Find the length of the word chosen by the computer.
word_length = len(computer_choice)


# Here is the end_of_game bolean test which will end the game 
# if it changes from the its predefined value which is False at the beginning.
end_of_game = False

# Here is lives variable which will detect how many mistakes the user made in the game.
lives = 6


# Here we declare a variable called display which will show us underscores
# which are letter being replaced by the letter you guess.
display = []
for symbol in range(word_length):
    display.append("_")


while not end_of_game:
    guess = input("Enter a letter: ").lower()
    
    # And also if the guessed letter is in the display u don't need to 
    # add another so u jump to guess the next one.
    if guess in display:
        print(f"You already guessed this '{guess}' letter.")
    
    for position in range(word_length):
        if  guess == computer_choice[position]:
            display[position] = computer_choice[position]
    
    
    # check if the guessed letter is the correct one 
    # and if its not let the user lose one live.
    if guess not in computer_choice:
        print(f"'{guess}' is not in the word. You lose a live!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You  lose!")
    
    # changing into string.
    print(" ".join(display))
    
    # This is to end the game which means the user guessed all the letters in the word.
    if "_" not in display:
        end_of_game = True
        print("You win!")
        
    # letting the user to play the game interactively
    # so I imported above some modules which will help me to 
    # make it more interactive and friendly.
    # one of them is printing the stages the game will take.
    print(stages[lives])
    