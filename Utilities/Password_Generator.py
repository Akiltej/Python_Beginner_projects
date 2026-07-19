alphabets = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
special=["!","@","#","$","%","^","&","*"]
#these are lists to be used in the generator
print("Welcome To The Password Generator")
a=int(input("How many alphabets in the password:"))
n=int(input("How many numbers in the password:"))
s=int(input("How many special signs in the password:"))

import random 
alphabet_selection=random.sample(alphabets,a)
number_selection=random.sample(numbers,n)
special_selection=random.sample(special,s)
#random.sample picks random characters from a pre defined list
p=(alphabet_selection + number_selection + special_selection)
#"".join allows us to join several lists together to form one word
random.shuffle(p)
#dont assing random.shuffle to a variable like this a=random.shuffle(p) as randome.shuffle returns the value none and you cant iterate none
password="".join(p)
print(password)