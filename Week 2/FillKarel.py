from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    pass
    while(no_beepers_present()):
        fill_row()
        
   


def fill_row():
    if front_is_clear():
        put_beeper()
        while (front_is_clear()):
            move()
            put_beeper()
    turn_around()
    back_to_wall()
    next_row()
    
def turn_around():
    turn_left()
    turn_left()
    
def back_to_wall():
    while(front_is_clear()):
        move()

def next_row():
    turn_left()
    turn_left()
    if left_is_clear():
        turn_left()
        move()
        turn_right()
    else:
        while(front_is_clear()):
            move()

def turn_right():
    for i in range (3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()