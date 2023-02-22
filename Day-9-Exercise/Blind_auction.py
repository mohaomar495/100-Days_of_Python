# this below code can only run by replit since the clear function is found the replit library so clear the console is coming in day 15. but now u can run it in replit. Thanks.
from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
# Here declaring empty dict and declaring a finishing variable.
bidders_dict = {}
bid_finish = False

#this function calculates the highest bidder of all the bidders
def highest_bidder(bidders):
      highest = 0
      winner = ""
      for bidder in bidders_dict:
        if bidders[bidder] > highest:
          highest = bidders[bidder]
          winner = bidder
      print(f"the winner is {winner} with a bid of ${highest}")

# This loop will run until bid_finish turns into False.
while not bid_finish:
  name = input("what's your name: ")
  amount = int(input("amount to bid: $"))
  #here is main function which calls other functions
  def main():
    bidders(name)

  #here is a function that adds our empty dict some elements
  def bidders(name):
      bidders_dict[name] = amount

  #calling this function will call all other functions that is being called inside that one.
  main()

  #asks whether there are other bidder who is remianing who need to bid.
  bidders_choice = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  # this is based on users choice if no it will finish the code and return the highest bidder. but if yes it will clear the console and starts the game from scratch.
  if bidders_choice == "no":
    bid_finish = True
    highest_bidder(bidders_dict)
  elif bidders_choice == "yes":
    clear()
    