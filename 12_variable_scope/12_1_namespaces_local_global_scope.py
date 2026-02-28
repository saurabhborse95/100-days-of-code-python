enemies = 1

def increase_enemies():
    enemies = 2                     # this never comes out of the scope of the function
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)          # this can't access the potion_strength variable

#### Global Scope

player_health = 10      # global variable


def drink_potion():
    potion_strength = 2         # local variable
    print(player_health)            # global variable

drink_potion()

### Namespace: anything that has a name (variable) has a namespace, but it is valid depending upon if it is local or global scope