#House for 20x20 world

from karel.stanfordkarel import *

def main():

    move()
    move()
    turn_left()
    move()
    move()
    for i in range(15):
        put_beeper()
        move()
    put_beeper()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    for i in range(15):
            put_beeper()
            move()
    turn_left()
    put_beeper()
    move()
    turn_left()
    for i in range(7):
            put_beeper()
            move()
    move()
    for i in range(7):
            put_beeper()
            move()
    put_beeper()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    for i in range(8):
            put_beeper()
            move()
    move()
    for i in range(6):
            put_beeper()
            move()
    turn_left()
    put_beeper()
    move()
    turn_left()
    for i in range(7):
            put_beeper()
            move()
    move()
    for i in range(7):
            put_beeper()
            move()
    put_beeper()
    move()
    turn_left()
    paint_corner("red")   # paint the starting corner red
    move()
    paint_corner("red")   # paint the starting corner red
    move()                # move to the next corner
    paint_corner("red") # paint the second corner green
    move()                # move to the third corner
    paint_corner("red")  # paint the third corner blue
    move()                # move to the fourth corner
    paint_corner("red")
    
# don't change this code
if __name__ == '__main__':
    main()