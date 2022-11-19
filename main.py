from replit import clear
#HINT: You can call clear() to clear the output in the console.

bid_list = {}
bid_done = False


def highest_bid(bid_list):
  highest_bid = 0
  winner = ""
  for bidder in bid_list:
    bid_amount = bid_list[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")
      
    





from art import logo
print(logo)

while not bid_done:
  name = input("What's your name?: ")
  bid = int(input("What's your bid?:$ "))
  bid_list[name] = bid
  further = input("Is there any other bidder? Yes or No:").lower()
  if further == "no":
    bid_done = True
    highest_bid(bid_list)
  elif further == "yes":
    clear()