from karel.stanfordkarel import *

def main():
    makeWaves()
    newPosition()
    makeWaves()
    newPosition()
    makeWaves()
    newPosition()
    makeWaves()
    
def makeWaves():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    
def newPosition():
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    move()
    

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()