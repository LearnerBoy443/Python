alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#doing the encryption
def encrypt(normal_text,shift_number):
    new_text='' #taking a new variable
    for letters in normal_text: #the letters will loop through the text and find the letter one by one
        position=alphabet.index(letters) #getting the index for each letter
        new_position=position+shift_number #getting shifted
        new_text+=alphabet[new_position] # assigning the new position in previous variable
    print(f"The encoded text is {new_text}")
# calling the function
encrypt(normal_text=text,shift_number=shift)


    
#doing the decryption
def decrypt(encrypted_text,shift_number1):
    decrypt_text=''
    for j in encrypted_text:
        position=alphabet.index(j)
        decrypted_text=position-shift_number1
        decrypt_text+=decrypted_text
    print(f"The Decrypted text is{decrypted_text}")

print(x=input("Do you want to decrypt the code?Yes or No"))
f direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)
