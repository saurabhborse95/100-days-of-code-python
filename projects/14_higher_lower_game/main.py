import art
from game_data import data
import random


def person_selector():
    return random.choice(data)


gameOver = False
currentScore = 0
firstGame = True
while not gameOver:
    if firstGame:
        person_A = person_selector()
        person_B = person_selector()
        if person_B == person_A:
            person_B = person_selector()
    else:
        person_B = person_selector()
        if person_B == person_A:
            person_B = person_selector()

    print(art.logo)
    print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}")
    print(art.vs)
    print(f"Against B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}")
    user_response = input("Who has more followers? Type 'A' or 'B': ")
    print(f"You chose {user_response}")
    if user_response == "A" and person_A['follower_count'] >= person_B['follower_count']:

        currentScore += 1
        print(f"You are right! Current Score: {currentScore}")
        person_A = person_A
    elif user_response == "B" and person_B['follower_count'] >= person_A['follower_count']:
        currentScore += 1
        print(f"You are right! Current Score: {currentScore}")
        person_A = person_B

    else:
        gameOver = True
        print(f"You lose! Game Over!   {person_A['name']} has {person_A['follower_count']} followers AND   {person_B['name']} has {person_B['follower_count']} followers  \n\n\n  Final Score: {currentScore}")


