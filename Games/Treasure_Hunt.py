print("Welcome to Treasure Island!\nYour mission is to find the Treasure")
option1=input("You have arrived at a crossroad do u want to turn LEFT or RIGHT---")
if option1=="LEFT":
    option2=input("you have reached a river , you can SWIM or WAIT---")
    if option2=="WAIT":
        option3=input("You have reached the chamber pick a door to go through---RED--BLUE--YELLOW--ORANGE--BLACK--WHITE:::")
        if option3=="RED":
            print("You got burnt by fire---GAME OVER---")
        elif option3=="BLUE":
            print("Eaten by beasts---GAME OVER---")
        elif option3=="YELLOW":
            print("You Found the Treasure!!!--WINNER--")
        else:
            print("Fallen into pit of snakes---GAME OVER---")
    elif option2=="SWIM":
        print("Eaten by Crocodile---GAME OVER---")
elif option1=="RIGHT":
    print("Fallen into a hole---GAME OVER---")
else:
    print("GAME OVER")