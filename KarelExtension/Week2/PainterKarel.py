from karel.stanfordkarel import *

"""
Karel should paint the whole world, any color you want. 
As an extension, have karel randomly paint each corner.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    paint()

def paint():
    while left_is_clear():
        paint_corner_randomly()
        move()
        paint_corner_randomly()
        if front_is_blocked():
            if facing_east():
                turn_left()
                move()
                turn_left()
            else:
                turn_left()
                turn_left()
                turn_left()
                move()
                turn_left()
                turn_left()
                turn_left()
        paint()


def paint_corner_randomly():
    if random():
        paint_corner("blue")
    else:
        paint_corner("green")
        
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()