from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
        
    x = random.randint(0, CANVAS_HEIGHT-SIZE)
    y = random.randint(0, CANVAS_WIDTH-SIZE)    
    start_x=0
    start_y=0
    
    player=canvas.create_rectangle(start_x, start_y, start_x+SIZE,start_y+SIZE,"blue")
    snake=canvas.create_rectangle(x, y, x + SIZE, y + SIZE,"red")    
    
    while (start_x+SIZE<CANVAS_WIDTH):
        start_x+=SIZE
        canvas.moveto(player, start_x, start_y)
        time.sleep(DELAY)
        
        
    
        

if __name__ == '__main__':
    main()