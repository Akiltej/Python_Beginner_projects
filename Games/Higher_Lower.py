import random
import os
print("Welcome to the Higher-Lower Game! Guess which celebrity has higher instagram followers by selecting either A or B!")
celebrities = [
    {"name": "Cristiano Ronaldo", "followers": 668000000},
    {"name": "Virat Kohli", "followers": 273000000},
    {"name": "Michael Jackson", "followers": 1600000},
    {"name": "Roger Federer", "followers": 13100000},
    {"name": "Lionel Messi", "followers": 509000000},
    {"name": "Selena Gomez", "followers": 405000000},
    {"name": "Dwayne Johnson", "followers": 382000000},
    {"name": "Kylie Jenner", "followers": 382000000},
    {"name": "Ariana Grande", "followers": 363000000},
    {"name": "Kim Kardashian", "followers": 344000000},
    {"name": "Beyoncé", "followers": 300000000},
    {"name": "Khloé Kardashian", "followers": 292000000},
    {"name": "Justin Bieber", "followers": 287000000},
    {"name": "Kendall Jenner", "followers": 278000000},
    {"name": "Taylor Swift", "followers": 273000000},
    {"name": "Jennifer Lopez", "followers": 240000000},
    {"name": "Neymar Jr", "followers": 236000000},
    {"name": "Miley Cyrus", "followers": 205000000},
    {"name": "Zendaya", "followers": 174000000}
]
game_score=0
game_over=False
while game_over==False:
    account_A=random.choice(celebrities)
    account_B=random.choice(celebrities)
    while account_A==account_B:
        account_B=random.choice(celebrities)
    account_A_name=account_A["name"]
    account_A_followers=account_A["followers"]
    account_B_name=account_B["name"]
    account_B_followers=account_B["followers"]
    print("A)",account_A_name,"---",account_A_followers)
    print("B)",account_B_name,"---N/A")
    guess=input("Enter Your Guess (A/B)---")
    if account_A_followers>account_B_followers and guess=="A":
        print("Correct,you get one point")
        game_score+=1
        game_over=False
    elif account_A_followers>account_B_followers and guess=="B":
        print("Wrong,Game Over")
        print("Your Final Score is:",game_score)
        game_over=True
    elif account_A_followers<account_B_followers and guess=="A":
        print("Wrong,Game Over")
        print("Your Final Score is:",game_score)
        game_over=True
    elif account_A_followers<account_B_followers and guess=="B":
        print("Correct,you get one point")
        game_score+=1
        game_over=False
    print("-------------------------------------------------------------------------------")



