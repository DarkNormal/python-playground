from turtle import Turtle, Screen
import time


if __name__ == '__main__':
    game_is_on = True
    screen = Screen()
    screen.tracer(0)
    screen.setup(width=500, height=500)
    screen.bgcolor("black")
    screen.title("Shnake game")

    starting_postions = [(0, 0), (-20, 0), (-40, 0)]

    segments = []
    for coord in starting_postions:
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(coord)
        segments.append(t)
    screen.update()
    while game_is_on:
        for seg_num in range(len(segments) - 1, 0, -1):
            segment = segments[seg_num]
            next_segment = segments[seg_num - 1]
            segment.setposition((next_segment.xcor(), next_segment.ycor()))
        segments[0].left(90)
        segments[0].forward(20)
        screen.update()
        time.sleep(0.2)
    screen.exitonclick()
