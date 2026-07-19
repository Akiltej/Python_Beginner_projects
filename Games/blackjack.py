import random 
def deal_card():
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        card=random.choice(cards)
        return card 
def calculate_score(cards):
        if sum(cards)==21 and len(cards)==2:
                return 0
        if 11 in cards and sum(cards)>21:
                cards.remove(11)
                cards.append(1)
        return sum(cards)
def compare(user_score,comp_score):
        if user_score==comp_score:
                print("Its a draw")
        elif comp_score==0:
                print(f"Lose,Opponent has blackjack\n computer has{comp_cards}")
        elif user_score==0:
                print("Win , You have Blackjack")
        elif user_score>21:
                print("Lose,You went over 21")
        elif comp_score>21:
                print(f"Win,Computer went over 21 \n computer has{comp_cards}")
        elif comp_score>user_score:
                print(f"Lose \n computer has{comp_cards}")
        else:
                print("Win")
user_cards=[]
comp_cards=[]
comp_score=-1
user_score=-1
game_over=False
for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
while game_over==False:
        user_score=calculate_score(user_cards)
        comp_score=calculate_score(comp_cards)
        print(f"your cards are{user_cards},current score:{user_score}")
        print(f"computers first card is {comp_cards[0]}")
        if user_score==0 or comp_score==0 or user_score>21:
                game_over=True
        else:
                user_should_deal=input("Type 'y' to get another card , 'n' to pass----")
                if user_should_deal=="y":
                        user_cards.append(deal_card())
                elif user_should_deal=="n":
                        game_over=True
while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_card())
        comp_score=calculate_score(comp_cards)
compare(user_score=user_score,comp_score=comp_score)



        