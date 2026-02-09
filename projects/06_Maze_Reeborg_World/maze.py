def turn_right():
    turn_left()
    turn_left()
    turn_left()

def motion():
    if wall_in_front():
        turn_left()
    if front_is_clear():
        move()
    if right_is_clear():
        turn_right()
        
     
        
while not at_goal():
    motion()
