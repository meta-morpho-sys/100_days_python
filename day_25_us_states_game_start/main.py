import turtle
import pandas as pd
from map_manager import MapManager


screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

correct_states = set([])
map_manager = MapManager()
states_data = pd.read_csv('50_states.csv')
all_states = states_data.state.to_list()


while len(correct_states) < 50:
    # Answer management
    guessed_states = len(correct_states)
    answer_state = screen.textinput(f"Guess the State({guessed_states}/50 States)",
                                    "What's another name of a state?").title()
    if answer_state == 'Exit':
        # Get all the names of the states which haven't been guessed
        states_to_learn = set(all_states) - correct_states
        new_data = pd.DataFrame(states_to_learn)
        # Write them in a `states_to_learn.csv`
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        ## check answer against the list of states
        correct_states.add(answer_state)
        state_data_row = states_data[states_data.state == answer_state]
        map_manager.update_map(state_data_row)
