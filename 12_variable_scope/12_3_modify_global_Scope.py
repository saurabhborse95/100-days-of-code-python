enemies = 1

def increase_enemies():                 # ONE MUST AVOID MODIFYING VARIABLES FROM GLOBAL Scope
    global enemies                  # this tells python to access the global variable and can modify it
    enemies += 1                   # python function cannot access the global variable for modification, it does not allow that
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

###===============================

## Better way of doing it


def increase_enemies(enemy):
    return enemy + 1

enemies = increase_enemies(enemies)

