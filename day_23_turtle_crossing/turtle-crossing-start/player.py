from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape("turtle")
        self.color('yellow')
        self.goto(STARTING_POSITION)
        self.left(90)
        self.new_level = "no"

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def detect_collision(self, cars):
        #   Detect collision with a car
        for car in cars:
            if self.distance(car) < 25:
                print("STRIKE")

    def return_to_start(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.new_level = 'yes'
            return self.new_level

