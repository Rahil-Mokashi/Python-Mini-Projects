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


tim.width(5)

tim.speed(10)
for i in range(36):
    tim.pencolor(color())
    tim.circle(100)
    tim.left(10)


screen = Screen()
screen.exitonclick()
