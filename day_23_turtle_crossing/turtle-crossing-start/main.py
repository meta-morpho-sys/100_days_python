import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Turtle Road Crossing")

player = Player()
car_manager = CarManager()

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
    player.return_to_start()
    car_manager.level_up()


screen.exitonclick()