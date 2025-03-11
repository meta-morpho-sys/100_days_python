from turtle import Turtle

FONT = ("Courier", 10, "bold")

class MapManager(Turtle):
    def __init__(self):
        super(MapManager, self).__init__()
        self.penup()
        self.color('red')

    def update_map(self, state_data):
        state = state_data.state.item()
        x_coor = state_data.x.item()
        y_coor = state_data.y.item()
        self.goto(x_coor,y_coor)
        self.write(state, align='left', font=FONT)

