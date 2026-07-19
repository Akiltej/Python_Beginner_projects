import random 
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_options=[rock,paper,scissors]
User=int(input("Choose 0 for rock---1 for paper---2 for scissors==="))
if User>=3 or User<0:
    print("Invalid Choice . YOU LOSE")
else:
    print(game_options[User])

    computer=random.randint(0,2)
    print("Computer chooses:")
    print(game_options[computer])

    if User==computer:
        print("DRAW")
    elif User==0 and computer==1:
        print("YOU LOSE")
    elif User==0 and computer==2:
        print("YOU WIN")
    elif User==1 and computer==0:
        print("YOU WIN")
    elif User==1 and computer==2:
        print("YOU LOSE")
    elif User==2 and computer==0:
        print("YOU LOSE")
    elif User==2 and computer==1:
        print("YOU WIN")