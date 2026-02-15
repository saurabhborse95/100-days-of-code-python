#### Caesar cipher discovered the encrpytion technique using shifts in the sequence
import string

## Shift = 0 --> A=A, B=B, C=C, ...

## Shift = 1 --> A=B, B=C, C=D, ...

## Shift = 3 --> A=C, B=D, D=E, ..

#### TODO-1     Create a function encrypt(), that takes the "original_text" and "shift_amount" as 2 inputs

#### TODO-2     Inside the encrypt() function, shift each letter of the original_text by the shift amount and print the encrypted texts

#### TODO-3     Call encrypt() fucntion and pass user input

#### TODO-4    What happens if you try to shift a forwards by 9? Can you fix the code?

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']



fruits = ["apples", "pears", "oranges"]

## indexing
# print(fruits.index("pears"))            # 1
# print(fruits.index("apples"))           # 0




def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        # position of the letter + shift
        shifted_position = alphabet.index(letter) + shift_amount
        ## if the shifted_position is more than the len(alphabet) --> using modulo operator --> if shifted_pos = 35 --> 35 % len(alphabet) --> 35 % 25 --> remainder --> 10 --> index of desired character
        ### if shifted position is less than len(aphabet) --> 5%25 --> 5

        shifted_position = shifted_position % len(alphabet)
        encrypted_text += alphabet[shifted_position]



    print(f"Here is the encoded result: {encrypted_text}")



direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
original_text = input("Type your message: \n").lower()
shift = int(input("Type your shift amount: \n"))

encrypt(original_text, shift)
