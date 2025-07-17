import turtle as t
from turtle import Screen
import random as ran

t.colormode(255)

direction = [0, 90, 180, 270]

tim = t.Turtle()
tim.shape("classic")

tim.width(7)
tim.speed("fastest")
for i in range(250):
    r = ran.randint(0, 255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    tim.pencolor((r,g,b))
    tim.setheading(ran.choice(direction))
    tim.forward(20)


screen = Screen()
screen.exitonclick()

