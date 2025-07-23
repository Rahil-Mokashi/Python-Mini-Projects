from turtle import Turtle, Screen 
import random as ran 

screen = Screen()

screen.setup(width=600, height=600)

race_is_on = False

rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

y_positions = [150, 100 , 50, 0, -50, -100, -150]

all_turtles = []

user_choice = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color: ")

for i in range(7):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(rainbow_colors[i])
    turtle.goto(x=-290,y=y_positions[i])
    all_turtles.append(turtle)
    
if user_choice:
    race_is_on = True
while race_is_on:
      
    for turtle in all_turtles:
        
        if turtle.xcor() > 280:
            winner = turtle.pencolor()
            if user_choice == winner:
                print(f"You win, {user_choice} is the winner!")
                race_is_on = False
            else:
                print(f"You Lose, {winner} is the winner!")
                race_is_on = False
        
        random_distance = ran.randint(0, 10)
        turtle.forward(random_distance)
    
screen.bye()






