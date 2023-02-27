def calculate_score(cards):
    """Returns the summation of the items in given list."""
    sum = 0
    for card in cards:
        if 11 in cards and 10 in cards and len(cards) == 2:
            return 0
        
        sum += card
        if 11 in cards and sum >= 21:
            sum = 0
            cards.remove(11)
            cards.append(1)
            for card in cards:
                sum += card
    return sum