import random
from art import print_logo
print_logo()
print("Welcome to the Number Guessing Game!\n")
def print_attempts(n, total):
    print(f"You have {total - n} attempts remaining to guess the number")



difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()

if difficulty == "easy":

    number_of_attempts = 10
    print(f"You chose the difficulty level : {difficulty}. You have {number_of_attempts} attempts to guess the number")
elif difficulty == "medium":
    number_of_attempts = 7
    print(f"You chose the difficulty level : {difficulty}. You have {number_of_attempts} attempts to guess the number")
elif difficulty == "hard":
    number_of_attempts = 5
    print(f"You chose the difficulty level : {difficulty}. You have {number_of_attempts} attempts to guess the number")
else:
    print("Please type easy, medium or hard correctly")
    exit()

print(f"You chose {difficulty}. You have {number_of_attempts} attempts.")

number_to_be_guessed = random.randint(1, 100)
print(f"Number is {number_to_be_guessed}")

game_over = False
attempt = 0
while attempt < number_of_attempts and not game_over:
    try:
        input_number = int(input("Make a guess between 1 and 100: "))
    except ValueError:
        print("Please type a >>>number<< between 1 and 100-> Try Again!!!!")
        continue
    if not 1 <= input_number <= 100:
        print("Number must be between <<<1 and 100<<<! -> Try Again!!!!")
        continue

    attempt += 1
    if input_number == number_to_be_guessed:
        game_over = True
        print(f"Congratulations! You guessed the right number! : {number_to_be_guessed}")
    elif input_number < number_to_be_guessed:
        print("Too low!")  #
        print_attempts(attempt, number_of_attempts)
    elif input_number > number_to_be_guessed:
        print(f"Too high!")
        print_attempts(attempt, number_of_attempts)

if not game_over:
    print("You lost the game!")
