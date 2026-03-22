bids = {}
continue_bidding = True

# Taking input from users
while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        continue_bidding = False
    else:
        print("\n" * 20)  # Clears screen (simple way)


# Function to find highest bidder
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Calling the function
find_highest_bidder(bids)
