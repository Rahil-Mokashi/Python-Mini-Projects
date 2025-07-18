import turtle as t
from turtle import Screen
import colorgram as cg
import random as ran

t.colormode(255)
tim = t.Turtle()
tim.shape("classic")
tim.speed("fastest")
screen = Screen()
tim.penup()
screen.setup(width=600, height=600)

colors = cg.extract('hirst_spot.webp', 100)
all_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    all_colors.append((r,g,b))
    

tim.setheading(225)
tim.fd(50*7)
tim.setheading(0)

for dot_count in range(1, 122):
    tim.dot(20, ran.choice(all_colors))
    tim.fd(50)
    
    
    if dot_count %11 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(50*11)
        tim.setheading(0)
   
tim.hideturtle() 
tim.home()

screen.exitonclick()

