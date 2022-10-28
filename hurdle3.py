def turn_right():
   turn_left()
   turn_left()
   turn_left() 
    
def blockjump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def wall():
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
    
while not at_goal():
    if wall_in_front():
        wall()
    else:
        move()

