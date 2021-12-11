from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def move(self):
        xcor = self.xcor() + 10
        ycor = self.ycor() + 10
        if(xcor < 350 and ycor < 350):
            self.goto((xcor, ycor))

