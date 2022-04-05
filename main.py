import turtle
import pandas

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

user_answer = screen.textinput(title="Guess a US state", prompt="Type in below a US state you can think of")














screen.exitonclick()