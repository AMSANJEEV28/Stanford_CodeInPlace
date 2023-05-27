from graphics import Canvas

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # animation loop 
    while True:
        # get the locations of the mouse
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        # check that the mouse location is in bounds
        if mouse_x >= 0 and mouse_x <= CANVAS_WIDTH and mouse_y >=0 and mouse_y <= CANVAS_HEIGHT:
            
            # draw a circle for where the mouse is
            canvas.create_oval(mouse_x, mouse_y, mouse_x + CIRCLE_SIZE, mouse_y + CIRCLE_SIZE, 'cyan')
        
        # typical animation loop code 
        # canvas.mainloop()  # Ignore this line for current solutions.
        time.sleep(DELAY)


if __name__ == "__main__":
    main()