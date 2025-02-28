from turtle import Turtle

FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard,self).__init__()
        self.penup()
        self.hideturtle()
        self.color("yellow")
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 260)
        self.write(f"Level: {self.level}", False, "left", FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()


    def end_game(self):
        self.clear()
        self.home()
        self.write("END OF GAME")
