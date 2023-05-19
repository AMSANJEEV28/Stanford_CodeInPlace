from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_random_circles(canvas)
    
    
def draw_random_circles(canvas):
    for i in range(N_CIRCLES):
        x = random.randint(0, CANVAS_HEIGHT-CIRCLE_SIZE)
        y = random.randint(0, CANVAS_WIDTH-CIRCLE_SIZE)
        color = random_color()

        print(x,y,color)
        canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, random_color())

def random_color():
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()