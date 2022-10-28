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
    
while not at_goal():
    blockjump()

