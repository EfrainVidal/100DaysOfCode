from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

# Create the Screen
screen = Screen()
screen.title("Pong Game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)  # turn off animation

scoreboard = Scoreboard()

r_paddle = Paddle((375, 0))
l_paddle = Paddle((-375, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # slows the animation per pixel
    screen.update()  # turn on animation
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 342 or ball.distance(l_paddle) < 50 and ball.xcor() < -342:
        ball.bounce_x()

    # Detect if R paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if L paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
