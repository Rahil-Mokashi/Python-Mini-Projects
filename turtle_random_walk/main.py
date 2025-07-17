import turtle as t
from turtle import Screen
import random as r

colors = [
    "red", "blue", "green", "orange", "purple", "yellow", "pink",
    "cyan", "magenta", "lime", "maroon", "navy", "teal", "violet",
    "brown", "gold", "silver", "coral", "turquoise", "indigo"
]

direction = [0, 90, 180, 270]

tim = t.Turtle()
tim.shape("classic")

tim.width(7)
tim.speed("fastest")
for i in range(250): 
    tim.pencolor(r.choice(colors))
    tim.setheading(r.choice(direction))
    tim.forward(20)


screen = Screen()
screen.exitonclick()

