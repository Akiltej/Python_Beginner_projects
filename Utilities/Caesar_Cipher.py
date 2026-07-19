rerun=True 
while rerun==True:
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    mode=input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text=input("Enter your message\n:").lower()
    shift=int(input("Enter your shift amount\n"))

    def encrypt(original_text,shift_amount):
        cipher_text=""
        for letter in original_text:
            if letter in alphabets:
                shifted_position=(alphabets.index(letter) + shift_amount)%26
                cipher_text+=alphabets[shifted_position]
            else:
                cipher_text+=letter
        print(f"Here is the encoded text:{cipher_text}")

    def decrypt(original_text,shift_amount):
        cipher_text=""
        for letter in original_text:
            if letter in alphabets:
                shifted_position=(alphabets.index(letter) - shift_amount)%26
                cipher_text+=alphabets[shifted_position]
            else:
                cipher_text+=letter
        print(f"Here is the decoded text:{cipher_text}")


    if mode=="encode":
        encrypt(original_text=text,shift_amount=shift)
    elif mode=="decode":
        decrypt(original_text=text,shift_amount=shift)

    choice=input("Do you want to go again (y/n)??")
    if choice=="y":
        rerun=True
    elif choice=="n":
        rerun=False
        print("Program terminated")

    
        
           