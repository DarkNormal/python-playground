from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for coord in STARTING_POSITIONS:
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(coord)
            self.segments.append(t)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[seg_num]
            next_segment = self.segments[seg_num - 1]
            segment.setposition((next_segment.xcor(), next_segment.ycor()))
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        print("up called")
        self.head.setheading(90)

    def down(self):
        print("down called")
        self.head.setheading(270)

    def left(self):
        print("left called")
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
