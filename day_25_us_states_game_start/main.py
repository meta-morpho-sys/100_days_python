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


while len(correct_states) < 50:
    # Answer management
    guessed_states = len(correct_states)
    answer_state = screen.textinput(f"Guess the State({guessed_states}/50 States)",
                                        "What's another name of a state?").title()
    if answer_state:
        # Answer Management
        states_data = pd.read_csv('50_states.csv')
        try:
            ## check answer against the list of states
            correct_answer = states_data[states_data.state == answer_state]
            correct_states.append(correct_answer)
            ## if correct write on the map
            map_manager.update_map(correct_answer)
        except ValueError as e:
            print(e)


screen.exitonclick()
