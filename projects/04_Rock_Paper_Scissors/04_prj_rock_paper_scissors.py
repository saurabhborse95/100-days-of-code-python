import random

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock Paper Scissors game!\n-----------\n")

choices = [rock, paper, scissors]
user_input = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors: "))


if user_input < 0 or user_input > 2:        # checking for invalid responses
    print("Invalid input. Game Over")
    exit()

print("You chose:")
print(choices[user_input])          # displaying the user choice





computer_choice = random.randint(0,2)

print("Computer chose:")
print(choices[computer_choice])


if user_input == computer_choice:
    print("It's a Draw 🤝")

elif user_input == 0 and computer_choice == 2:      # Winning scenarios
    print("You Won!!!")
elif user_input == 1 and computer_choice == 0:
    print("You Won!!!!")
elif user_input == 2 and computer_choice == 1:
    print("You Won!!!!")
else:
    print("You Lose!!!")

