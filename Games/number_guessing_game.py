import random
import os
print("-----Welcome To The Number Guessing Game-----")
difficulty=input("Which Diffuculty Would You Like to Play On?(easy(10 turns)/hard(5 turns)):").lower()
chosen_number=random.randint(1,100)
if  difficulty=="easy":
    i=0
    while i<10:
        guess=int(input("Enter your guess:"))
        if guess==chosen_number:
            print("YOU HAVE GUESSED CORRECTLY! YOU WIN!!!")
            exit()
        elif guess>chosen_number:
            print("Too High.")
        elif guess<chosen_number:
            print("Too Low.")
        else:
            print("You rand out of guesses.YOU LOSE!")
        i+=1
        if i==10:
            print("You ran out of turns.YOU LOSE!")
elif difficulty=="hard":
    i=0
    while i<5:
        guess=int(input("Enter your guess:"))
        if guess==chosen_number:
            print("YOU HAVE GUESSED CORRECTLY! YOU WIN!!!")
            exit()
        elif guess>chosen_number:
            print("Too High.")
        elif guess<chosen_number:
            print("Too Low.")
        
        i+=1
        if i==5:
            print("You ran out of Turns.YOU LOSE!")





