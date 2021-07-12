from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_axis = [-100, -50, 0, 50, 100, 150]
all_turtles = []

race_on = False

for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You got it right! The winning turtle is: {winning_turtle}")
            else:
                print(f"You got it wrong! The winning turtle is: {winning_turtle}")
        turle_forward = random.randint(1, 10)
        turtle.forward(turle_forward)

screen.exitonclick()
