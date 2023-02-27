from deal_card import deal_card
from calculate_score import calculate_score
from art import logo
print(logo)

user_cards = []
computer_cards = []

# this will add 2 random numbers to user_cards or computer_cards each.
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# when u hit the end of the game this will turn to True and then stops the while loop.
end_game = False

while not end_game:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"current cards {user_cards}, your current score is {user_score}")
    print(f"computer's first card is {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        end_game = True
    else:
        should_continue = input("type 'y' to get another card, type 'n' to pass: ").lower()
        if should_continue == "y":
            user_cards.append(deal_card())
        else:
            end_game = True

# this calculates computer's score after we calculate the user's score.
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    


def compare(user_score, computer_score):
    """Returns the status of the game."""
    if user_score == computer_score:
        print("Draw!")
    elif computer_score == 0:
        print("You lose!")
    elif user_score == 0:
        print("You win!")
    elif user_score > 21:
        print("You lose!")
    elif computer_score > 21:
        print("You win!")
    elif computer_score > user_score:
        print("You lose!")
    elif computer_score < user_score:
        print("You win!")

print(f"your final hand: {user_cards}, your final score: {user_score}")
print(f"computer's final hand: {computer_cards}, computer's final score: {computer_score}")

print(compare(user_score, computer_score))