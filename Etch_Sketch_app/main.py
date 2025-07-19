from turtle import Turtle, Screen 

tim = Turtle()
tim.width(3)
screen = Screen()
tim.speed("fastest")

def forward():
    tim.fd(10)

def backward():
    tim.backward(10)

def right():
    new = tim.heading() + 10
    tim.setheading(new)

def left():
    new = tim.heading() + 10
    tim.setheading(new)

def clean():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(forward, "w")
screen.onkeypress(backward, "s")
screen.onkeypress(right, "d")
screen.onkeypress(left, "a")
screen.onkey(clean, "c")

screen.exitonclick()