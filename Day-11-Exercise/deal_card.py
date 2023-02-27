import random

def deal_card():
    """Returns a random card from list of given cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_choice = random.randint(0, (len(cards) - 1))
    card = cards[random_choice]
    return card