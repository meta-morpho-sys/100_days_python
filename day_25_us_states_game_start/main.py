import turtle
import pandas as pd
from map_manager import MapManager


screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

correct_states = []
map_manager = MapManager()

is_game_on = True
while is_game_on:
    # Answer management
    answer_state = screen.textinput('Guess the State',"What's another name of a state?").title()
    # Answer Management
    ## check answer against the list of states
    states_data = pd.read_csv('50_states.csv')
    correct_answer = states_data[states_data.state == answer_state]
    ## if correct write on the map
    map_manager.update_map(correct_answer)
    correct_states.append(correct_answer)





screen.exitonclick()
