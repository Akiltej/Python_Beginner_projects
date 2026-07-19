import random 
print("******WELCOME TO HANGMAN******")
hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''',]
lives=6

word_list=["ALPHABET","BACKPACK","GINGER","LION","CANDY","CHOCOLATE","TEA","HONEY","INDIA","WATER","LEMON","BANANA","MELON","ORANGE","TIGER"]
Chosen_word=random.choice(word_list)
placeholder=""
length_word=len(Chosen_word)
for position in range(length_word):
    placeholder+="_"
print(placeholder) 
correct_letters=[]
game_over=False
while not game_over:
    guess=input("Enter A Letter---").upper()
    display=""
    for letter in Chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter 
        else:
            display+="_"
    print(display)
    if guess not in Chosen_word:
        lives-=1
        print(f"Wrong ,You have {lives} lives left.")
        if lives==0:
            game_over=True 
            print("💀You Lose💀")

    if "_" not in display:
        game_over=True
        print("🎉You Win🎉")
    print(hangman[lives])    