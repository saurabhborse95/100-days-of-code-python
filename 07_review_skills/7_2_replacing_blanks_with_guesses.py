import random
word_list = ["Zebra", "Monkey", "Burger", "Jakarta", "Amazon", "Banana", "Mango", "Lenovo", "Adidas", "Gemini", "Mercedes", "Toyota", "Lindt", "Velocity"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1 : create a "placeholder" with the same number of blanks as the chosen word
placeholder = ""

for pos in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)
#print("_" *len(chosen_word))

guessed_letter = input("Guess a letter: ").lower()


# TODO-2: Create a display variable that puts the letter in the right positions, but unguessed letters stay as _
display = ""

for letter in chosen_word:
    if letter == guessed_letter:
        display += letter

    else:
        display += "_"

print(display)