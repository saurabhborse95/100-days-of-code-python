## Rules

## If the total number of the sum of all card > 21 ----> YOU LOSE!!!

### Jack, King and Queen are counted as 10

### Ace can either count as 1 or a 11  --> You decide which value


import random
cards = [11, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_set):
    return sum(cards_set)


def computer_plays(computer_cards):
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
    return computer_cards


def display_result(user_cards, computer_cards):
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    print(f"Your final hand: {user_cards} , final score: {user_score}")
    print(f"Computer's final hand: {computer_cards} , final score: {computer_score}")
    if user_score == computer_score:
        print("Draw!")
    elif user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif user_score > computer_score:
        print("You won!")
    elif computer_score > user_score:
        print("Computer won! You Lose")


user_cards = []
computer_cards = [random.choice(cards)]

for i in range(0,2):
    user_cards.append(deal_card())
    # user_cards.append(random.choice(cards))
    # computer_cards.append(deal_card())

print(f"Your cards: {user_cards} , current score: {sum(user_cards)}")
print(f"Computer's first card: {computer_cards}")

play_further = input("Type 'y' to get another card, type 'n' to pass: ")
if play_further == "y":
    while play_further == "y":
        user_cards.append(random.choice(user_cards))
        if sum(user_cards) > 21:
            computer_cards = computer_plays(computer_cards)
            display_result(user_cards, computer_cards)
            print("You went over. You lose!")
            break
        elif sum(user_cards) < 21:
            print(f"Your cards: {user_cards} , current score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards}")
            play_further = input("Type 'y' to get another card, type 'n' to pass: ")


elif play_further == "n":
    computer_cards = computer_plays(computer_cards)
    display_result(user_cards, computer_cards)