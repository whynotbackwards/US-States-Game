from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
states_image = 'blank_states_img.gif'
screen.addshape(states_image)
screen.setup(width=725, height=491)

map_turtle = Turtle()
map_turtle.shape(states_image)

turtle_scribe = Turtle()
turtle_scribe.hideturtle()
turtle_scribe.penup()
turtle_scribe.speed(10)

states_df = pd.read_csv('50_states.csv')
states = states_df.state.to_list()
correct_states = []

nope = ''

while len(correct_states) < 50:
    guessed_state = screen.textinput(title=f"{len(correct_states)}/50 Correct",
                                     prompt=f"{nope}What's a{'nother' if len(correct_states) else ''} state's "
                                            f"name?:").title().strip()
    if guessed_state in ('Exit', 'Quit', 'Close'):
        break
    elif guessed_state in correct_states:
        nope = 'ALREADY GUESSED THAT ONE! '
        turtle_scribe.home()
    elif guessed_state in states:
        state_row = states_df[states_df.state == guessed_state]
        state_x = int(state_row.x)
        state_y = int(state_row.y)
        turtle_scribe.goto(state_x, state_y)
        turtle_scribe.write(guessed_state, align='center', font=('Courier', 10, 'bold'))
        correct_states.append(guessed_state)
        nope = ''
    else:
        nope = 'NOPE! '
        turtle_scribe.home()


missed_states = [state for state in states if state not in correct_states]
if not missed_states:
    missed_states = ['Congratulations! You know all your states!']
missed_states_df = pd.DataFrame(missed_states)
missed_states_df.to_csv('states_to_learn.csv')
