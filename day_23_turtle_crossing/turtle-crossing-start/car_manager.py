from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super(CarManager,self).__init__()
        self.cars = []
        self.car_prod_level = 10
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self,colour):
        car = Turtle("square")
        car.fillcolor(colour)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        return car

    def create_cars(self):
        rand_chance = random.randint(1, self.car_prod_level)
        if rand_chance == 2:
            car = self.create_car(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            car.goto(400, rand_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        print("Car Speed")
        print(self.car_speed)

    def increase_car_creation(self):
        self.car_prod_level -= 1


