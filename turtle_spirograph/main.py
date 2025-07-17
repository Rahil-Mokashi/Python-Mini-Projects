import turtle as t
from turtle import Screen
import random as ran

tim = t.Turtle()

t.colormode(255)

def color():
    r = ran.randint(0, 255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    color_combo = (r,g,b)
    return color_combo


tim.width(2)

tim.speed("fastest")

def drawing_spirograph(size):
    for i in range(int(360 / size)):
        tim.pencolor(color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)
        
drawing_spirograph(3)


screen = Screen()
screen.exitonclick()
