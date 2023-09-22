import turtle

import colorgram

# colors = colorgram.extract('image.jpg', 30)
# first_color = colors[0]
# list_colors = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r,g,b)
#     list_colors.append(new_color)
#
# print(list_colors)
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.penup()
# pos_y = -150
tim.speed("fastest")
tim.hideturtle()


color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
#
# for _ in range(10):
#     pos_y += 50
#     tim.sety(pos_y)
#     tim.setx(-150)
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
