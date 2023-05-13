from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.


def main():
    move()
    pick_up_all_beepers()

def move_to_wall():
    # Move until we hit the wall
    while front_is_clear():
        move()

def pick_up_all_beepers():
    # Pick up all the beepers on the first row
    while beepers_present():
        pick_beeper()
        pick_beeper()
        pick_beeper()
        pick_beeper()
        pick_beeper()
        pick_beeper()
        pick_beeper()
        pick_beeper()
        pick_beeper()
        pick_beeper()

        if front_is_clear():
            move()
            move()

def return_to_start():
    # Turn around
    turn_around()
    # Move to the end of the first row
    while front_is_clear():
        move()
    # Turn around again
    turn_around()

def turn_around():
    turn_left()
    turn_left()
   
   
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()