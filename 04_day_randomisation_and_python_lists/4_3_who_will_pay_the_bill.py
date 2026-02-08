import random

friends = ["Marco", "Carlo", "Bravo", "Serjio", "Perno", "Saltos", "Guro", "Eric", "Sara", "Susanna"]

# Option 1:
friend_to_pay = random.choice(friends)
print(f"The person who will pay the bill is : {friend_to_pay}")

# Option 2:
index = random.randint(0, len(friends))         # extracting a random index for the given list
print(f"random index is {index}")
print(f"the person who will pay the bill is : {friends[index]}")