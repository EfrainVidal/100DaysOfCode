from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # background color
screen.title("My Snake Game")  # title of game
screen.tracer(0)    # turn tracer off to make the screen smoother

snake = Snake()  # initialize a snake
food = Food()  # initialize a food item
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # update the screen to show snake smoother together
    time.sleep(0.1)  # delay the update time to see it better

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
