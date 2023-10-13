from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

game_is_on = True
blind_auction = {}

def highest_bidder(blind_auction):
  winner = ""
  for name in blind_auction:
    max = blind_auction[name]
    if blind_auction[name] > max:
      max = blind_auction[name]
    winner = name
  return (f"The winner is {winner} with a BID price of {max}")


while game_is_on:
  name = input("Enter your name: ").lower()
  bid_price = float(input("BID price: "))
  
  blind_auction[name] = bid_price

  next_person = input("Is there another person: yes or no: ").lower()
  
  if next_person == "no":
    clear()
    game_is_on = False
    print(highest_bidder(blind_auction))
  elif next_person == "yes" or next_person != "yes":
    clear()
