from time import sleep
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager,self).__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self,colour):
        car = Turtle()
        car.shape("square")
        car.fillcolor(colour)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        return car

    def create_cars(self):
        car = self.create_car(random.choice(COLORS))
        rand_y = random.choice([-250,-100, 0, 100, 250])
        car.goto(300, rand_y)
        self.cars.append(car)
        # for colour in COLORS:
        #     car = self.create_car(colour)
        #     self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

