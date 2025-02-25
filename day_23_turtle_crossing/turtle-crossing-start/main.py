import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Turtle Road Crossing")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #   Detect collision with a car
    player.detect_collision(car_manager.cars)
    new_level = player.return_to_start()
    if new_level == 'yes':
        scoreboard.increase_score()
        car_manager.level_up()


screen.exitonclick()