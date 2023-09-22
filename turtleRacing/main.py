import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
all_turtle = []

# y_positions = [-70, -40, -10, 20, 50, 80]
# for turtle_index in range(0, 6):
#     tim = Turtle(shape="turtle")
#     tim.penup()
#     tim.color(colors[turtle_index])
#     tim.goto(x=-230, y=y_positions[turtle_index])

y = -75
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 30
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()