from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")

timmy.pensize(5)

colors = {
    4: "red",
    5: "yellow",
    6: "violet",
    7: "pink",
    8: "brown",
    9: "blue",
    10: "orange",
    
}

def shape(no):
    timmy.pencolor(colors.get(no, "black"))
    for i in range(no):
        angle = 360 / no 
        timmy.forward(100)
        timmy.right(angle)
        
for i in range(4,11):
    shape(i)

timmy.forward(100)


screen = Screen()
screen.exitonclick()