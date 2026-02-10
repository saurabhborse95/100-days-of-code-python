import random
from hangman_words import word_list
from hangman_art import hangman_stages, logo



# TODO-1 : Update the word list to use the 'word_list' from hangman_words.py   ---> DONE
# TODO-2: Update the code to use the stages from the hangman_art.py     ----> DONE
# TODO-3: import the logo from hangman_art.py and print it at the start of the game   ----> DONE
# TODO-4: If the user has entered a letter they've already guessed -_> print the letter and let them know (we should not deduct life for this) --->
# TODO-5: if the letter is not in the chosen_word, print out the letter and let them know  (you guessed letter a, that's not in the word. You lose a life)  ---> DONE
# TODO-6: Update the print statements to let the user know how many lives are left      ---> DONE
# TODO-7: Update the print statements to give the user the correct word             ---> DONE
print("\n\n\n")
print(logo)
print("--------------------------------------------------------\n")
chosen_word = random.choice(word_list).lower()
print(chosen_word)

placeholder = ""

for pos in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)


lives = 6




game_over = False

history_of_correctly_guessed_letters = []

while not game_over:
    print(f"\n\n********************** {lives} / 6 LIVES REMAINING ******************************\n\n")
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in history_of_correctly_guessed_letters[0:-1]:
        print(f"You have already guessed the letter {guessed_letter} before ")
    display = ""

    for letter in chosen_word:
        if letter == guessed_letter:                # check if any letter in chosen word matches the guessed letter
            display += letter
            history_of_correctly_guessed_letters.append(letter)             # add the correclty guesssed letter to the history
        elif letter in history_of_correctly_guessed_letters:             # check if any letter in the chosen_word matches the history of guessed letters
            display += letter


        else:

            display += "_"




    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"You chose letter {guessed_letter}, this is not in the word.    ********************          You lose a life       ")

        print(hangman_stages[lives])
        if lives == 0:
            game_over = True
            print(f"\n\n===================   GAME OVER!!!  ============== \n\n ======================================= The word was {chosen_word}")


    if "_" not in display:
        game_over = True
        print(f"\n\n===================   YOU WIN!!   ================================================ \n\n ==========================>>>   Your guessed letter was {chosen_word}")





