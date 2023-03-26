import random
from game_data import data as dt
from art import logo
from art import vs
from replit import clear

# the clear method comes from replit where i previously coded this code
# before i converted or transfered to vs code.
# The function of clear() is to clear whenever we gues correctly.

# this formats the output.
def format(account):
    """ Format a function that formats the displayed content."""
    N = account['name']
    D = account['description']
    C = account['country']
    return f"{N}, a {D}, from {C}"


def Answer(user_guess, first_person, second_person):
    """Answer a function that checks whether the user's guess is correct."""
    if first_person > second_person:
        return user_guess == "A"
    else:
        return user_guess == "B"

print(logo)
end_game = True
score = 0
B = random.choice(dt)

while end_game:
    """Assigning the B to A inside the while loop it will update A every time we run and enter a correct guess to the previous B value."""
    A = B  # first person
    B = random.choice(dt)  # second person
    """This updates B whenever there  is equility of A and B."""
    while A == B:
        B = random.choice(dt)

    print(f"Compare A: {format(A)}")
    print(vs)
    print(f"Against B: {format(B)}")

    user_guess = input("who has more followers? Type 'A' or 'B': ").upper()
    correct = Answer(user_guess, A['follower_count'], B['follower_count'])

    clear()
    print(logo)
    if correct == True:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        end_game = False
        print(f"Sorry, that's wrong. Final score: {score}")