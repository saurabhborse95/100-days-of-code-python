#### FLOW CHART Programming
import random
word_list = ["Zebra", "Monkey", "Burger", "Jakarta", "Amazon", "Banana", "Mango", "Lenovo", "Adidas", "Gemini", "Mercedes", "Toyota", "Lindt", "Velocity"]

### 1. Choosing a random word from the word_list
### 2. Ask the user to guess a letter --> Make it lowercase
### 3. Check if the letter the user guessed (guessed_letter) is in the chosen word -> print Truee or false respectively

chosen_word = random.choice(word_list)
# print(chosen_word)
guessed_letter = input("Guess a letter: ").lower()
# print("You guessed letter", guessed_letter)
for letter in chosen_word:

    if guessed_letter in chosen_word:
        print("True")
    else:
        print("False")



