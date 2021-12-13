from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 3
        self.y_move = 3

    def move(self):
        xcor = self.xcor() + self.x_move
        ycor = self.ycor() + self.y_move
        self.goto((xcor, ycor))

    def bounce(self):
        print("bounce!")
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
