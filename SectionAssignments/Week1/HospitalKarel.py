from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        if beepers_present():
            build_hospital()
        safe_move()


def build_hospital():
    pick_beeper()
    do_one_column()
    move()
    do_one_column()


def do_one_column():
    turn_left()
    put_three_beepers()
    return_to_base()
    turn_left()


def put_three_beepers():
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()


def return_to_base():
    turn_around()
    move_to_wall()


def move_to_wall():
    while front_is_clear():
        move()

def safe_move():
    if front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()
    
if __name__ == '__main__':
    main()