from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def build_stone():
    turn_left()
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
        
def next_stop():
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    for i in range(3):
        move()
    
    
def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    
    build_stone()
    next_stop()
    build_stone()
    next_stop()
    build_stone()
    next_stop()
    build_stone()
    turn_left()
    turn_left()
    move()
    move()
    move()
    move()
    turn_left()
        

if __name__ == '__main__':
    main()