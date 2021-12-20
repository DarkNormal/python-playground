from turtle import Turtle
import random


class Car(Turtle):

    def __init__(self, color, speed):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.move_speed = speed
        self.goto((320, random.randint(-270, 270)))

    def move(self):
        self.backward(self.move_speed)



