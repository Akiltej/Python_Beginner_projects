import os
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print("---Welcome to the Blind Auction Program!---")
Auction_Over=False
Auction_Book={}
while Auction_Over==False:
    bidder=input("Enter your name:")
    bid_amount=int(input("Enter Your Bid amount="))
    Auction_Book[bidder]=bid_amount
    persons=input("Anyone else wants to Bid? Type 'yes' or 'no'\n")
    if persons=="yes":
        Auction_Over=False
        clear_screen()
    elif persons=="no":
        Auction_Over=True
        bid_winner=max(Auction_Book,key=Auction_Book.get)
        print(f"The winner is {bid_winner} with a total bid of {Auction_Book[bid_winner]}$ ")




