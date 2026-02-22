## Rules

## If the total number of the sum of all card > 21 ----> YOU LOSE!!!

### Jack, King and Queen are counted as 10

### Ace can either count as 1 or a 11  --> You decide which value


import random
from art import print_blackjack_logo
from _pyrepl.commands import clear_screen


# cards = [11, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_set):
    """Returns the sum of the scores of the cards entered in cards_set."""
    if sum(cards_set) == 21 and len(cards_set) == 2:            # checking for blackjack
        return 0                # this will represent a blackjack in the game
    if sum(cards_set) > 21 and 11 in cards_set:
        # idx = cards_set.index(11)
        # cards_set[idx] = 1
        cards_set.remove(11)
        cards_set.append(1)
    return sum(cards_set)

def compare(u_score, c_score):
    if u_score == c_score:
        print("=================   IT'S A DRAW    =========================")

    elif c_score == 0:
        print("=================   YOU LOSE! Computer has a Blackjack!   =========================")

    elif u_score == 0:
        print("=================   YOU WIN ! You have a Blackjack!   =========================")
    elif u_score > 21:
        print("=================   YOU LOSE! YOU WENT OVER   =========================")
    elif c_score > 21:
        print("=================   YOU WIN! Computer went over!   =========================")
    elif u_score > c_score:
        print("=================   YOU WIN!   =========================")
    else:
        print("=================   YOU LOSE!   =========================")
def clr_screen():
    print("\n" * 20)


def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1             # default value
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, final score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            is_game_over = False
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        """Computes the computers game"""
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n *** **** **** *** **** *** *********  ** * ** **\n")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("\n *** **** **** *** **** *** *********  ** * ** **\n")
    compare(user_score, computer_score)
print_blackjack_logo()
while input("Do you want to play a game of BlackJack? Type 'y' or 'n'  : ") == "y":
    clr_screen()
    print_blackjack_logo()
    play_game()