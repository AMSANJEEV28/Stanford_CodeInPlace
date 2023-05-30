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
    
    # TODO: your code here
    
    x = random.randint(0, CANVAS_HEIGHT-SIZE)
    y = random.randint(0, CANVAS_WIDTH-SIZE)    
    start_x=0
    start_y=0
    
    color="blue"
    player=canvas.create_rectangle(start_x, start_y, start_x+SIZE , start_y+SIZE, color)
    goal=canvas.create_rectangle(x, y, x + SIZE, y + SIZE,"red") 
    
    while (start_x<CANVAS_WIDTH + SIZE):

        canvas.moveto(player, start_x, start_y)
        time.sleep(DELAY)
        key = canvas.get_last_key_press()
        
        if key == 'ArrowUp':
            start_y -= SIZE
        elif key == 'ArrowDown':
            start_y += SIZE
        elif key == 'ArrowLeft':
            start_x -= SIZE
        elif key == 'ArrowRight':
            start_x += SIZE
    
        xPlayer = canvas.get_left_x(player)
        yPlayer = canvas.get_top_y(player)        
        
        xGoal = canvas.get_left_x(goal)
        yGoal = canvas.get_top_y(goal)
        print (xPlayer, xGoal)
        
        
        if xPlayer > 380 or yPlayer > 380 or xPlayer <0 or yPlayer <0:
            canvas.set_color(player, "black")
            
            x = random.randint(0, CANVAS_HEIGHT - SIZE)
            y = random.randint(0, CANVAS_WIDTH - SIZE)
            canvas.moveto(goal, x, y)
        
if __name__ == '__main__':
    main()