from turtle import Turtle

FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard,self).__init__()
        self.penup()
        self.hideturtle()
        self.color("yellow")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 260)
        self.write(self.score,False, 'center', FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()


