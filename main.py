#ADS ANTOINE 
from turtle import Turtle, Screen, colormode
import random
import colorgram
import argparse
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process image path.')
    parser.add_argument('--image', type=str, help='Path to the image')
    parser.add_argument('--nmb_of_colors', type=int, help='Number of colors to extract from the image')
    parser.add_argument('--rows', type=int, help='Number of rows')
    parser.add_argument('--cols', type=int, help='Number of columns')
    parser.add_argument('--width', type=int, help='Width of the screen')
    parser.add_argument('--height', type=int, help='Height of the screen')
    parser.add_argument('--output', type=str, help='Output file name')
    args = parser.parse_args()
    
    WIDTH = args.width if args.width else 350
    HEIGHT = args.height if args.height else 350
    
    if not args.image:
        print('Please provide an image path with --image')
        exit()
        
    img_path = args.image
    
    nmb_of_colors = args.nmb_of_colors if args.nmb_of_colors else 30
    colors = colorgram.extract(img_path, nmb_of_colors)
    
    RGB_COLORS = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        RGB_COLORS.append((r,g,b))
            
    colormode(255)

    screen = Screen()

    screen.setup(width=WIDTH, height=HEIGHT)

    tim = Turtle()
    tim.speed("fastest")
    
    tim.penup()
    tim.hideturtle()
    tim.setposition(-130,-130)
    tim.setheading(0)
    
    rows = args.rows if args.rows else 10
    cols = args.cols if args.cols else 10
    
    for c in range(rows):
        for _ in range(cols):
            tim.dot(20, random.choice(RGB_COLORS))
            tim.forward(30)
        tim.setheading(90)
        tim.forward(30)
        tim.setheading(180)
        tim.forward(cols*30)
        tim.setheading(0)
     
    if args.output:
        screen.getcanvas().postscript(file=args.output)
        print(f'Image saved as {args.output}')
        time.sleep(10)
        screen.bye()
    else:
        screen.exitonclick()