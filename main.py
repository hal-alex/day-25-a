import turtle
import pandas
from turtle_state import Turtle_state

# Steps:
# Convert the guess to title case
# Check if the guess is among the top 50 states
# Write the correct guesses onto the map
# Use a loop to allow a user to keep guessing
# Record the correct guesses in a list
# Keep track of the score


screen = turtle.Screen()
screen.title("US Guess-a-state Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

all_of_states = pandas.read_csv("50_states.csv")

list_of_states = all_of_states["state"].to_list()

correct_guesses = []

check = all(item in correct_guesses for item in all_of_states)

while check == False:
    user_answer = screen.textinput(title=f"Guess a US state - {len(correct_guesses)}/{len(all_of_states)}",
                                   prompt="Type in below a US state you can think of").title()
    check = all(item in correct_guesses for item in all_of_states)
    for state in list_of_states:
        if user_answer == state:
            x_cor = int(all_of_states.loc[all_of_states.state == f"{state}", "x"])
            y_cor = int(all_of_states.loc[all_of_states.state == f"{state}", "y"])
            Turtle_state(state, x_cor, y_cor)
            correct_guesses.append(state)









screen.exitonclick()