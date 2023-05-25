from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car(canvas,x,y)
    #gave draw_car the parameters

    x = 100
    y = 100
    draw_car(canvas,x,y)
    #gave draw_car the parameters

def draw_car(canvas,x,y):
    #gave draw_car the parameters
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()