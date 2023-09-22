import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
# timmy.shape("turtle")
# timmy.color("Blue")

# timmy.pensize(5)
# directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r,g,b)
    return my_tuple
 
timmy.speed("fastest")

def draw_spiro(size_gap):
    for _ in range(int(360 / size_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_gap)

draw_spiro(5)

# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# colors = ["Red", "Blue", "Green", "Purple", "Black", "Brown", "Orange"]


# sides = 3
# while sides != 11:
#     timmy.color(random.choice(colors))
#     angle = 360 / sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#     sides += 1
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()