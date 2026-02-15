import random


word_list = ["Zebra", "Monkey", "Burger", "Jakarta", "Amazon", "Banana", "Mango", "Lenovo", "Adidas", "Gemini", "Mercedes", "Toyota", "Lindt", "Velocity"]

chosen_word = random.choice(word_list).lower()
print(chosen_word)


placeholder = ""

for pos in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

# TODO-1 : Use a while loop to let the user guess again
# TODO-2: Change the for loop so that you can keep the previously corrected "display"


game_over = False

history_of_correctly_guessed_letters = []

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guessed_letter:                # check if any letter in chosen word matches the guessed letter
            display += letter
            history_of_correctly_guessed_letters.append(letter)             # add the correclty guesssed letter to the history
        elif letter in history_of_correctly_guessed_letters:             # check if any letter in the chosen_word matches the history of guessed letters
            display += letter                                   # update the display

        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print(f"You win!! -->   Your guessed letter was {chosen_word}")





