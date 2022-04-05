import turtle
from turtle import Turtle

class Turtle_state():

    def __init__(self, state, x_cor, y_cor):
        self.state = state
        self.x_cor = x_cor
        self.y_cor = y_cor
        turtle_s = Turtle()
        turtle_s.hideturtle()
        turtle_s.penup()
        turtle_s.setposition(self.x_cor, self.y_cor)
        turtle_s.write(self.state)