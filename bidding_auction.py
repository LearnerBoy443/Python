import bidding_pic
bids={}
bidding_finished=False


def find_highest_bidder(bidding_record):
    bidding_records = {
        "Raj": 434,
        "Mukundu": 500,
        "Suraj": 600,
        "Abhirup": 1000
    }
    highest_bid = 0
    winner = ""
    for bidding in bidding_record:
       bidding_amount = bidding_records[bidding]
       if bidding_amount > highest_bid:
           highest_bid = bidding_amount
           winner = bidding
    print(
        f"The winner of the tournament is{bidding} with a highest bid of{highest_bid}")

while not bidding_finished:
    name=input("What is your name??")
    price=int(input("What is your bidding price?? $"))
    bids[name]=price
    should_continue=input("Is there any other bidder??Yes or NO")
    if should_continue=="NO":
        find_highest_bidder(bidding_record)
        bidding=False
