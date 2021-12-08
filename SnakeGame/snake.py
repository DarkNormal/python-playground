from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for coord in STARTING_POSITIONS:
            self.add_segment(coord)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[seg_num]
            next_segment = self.segments[seg_num - 1]
            segment.setposition((next_segment.xcor(), next_segment.ycor()))
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
