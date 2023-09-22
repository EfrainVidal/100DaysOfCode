from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)  # stop the animation

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)  # time the screen is refreshed
    screen.update()  # update the screen animation
    car.create_car()
    car.move_car()

    # Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when player reaches the end of the level
    if player.is_at_finish_line():
        player.start_level()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()
