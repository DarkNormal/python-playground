from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Shnake game")

starting_postions = [(0, 0), (-20, 0), (-40, 0)]
for coord in starting_postions:
    t = Turtle(shape="square")
    t.color("white")
    t.goto(coord)


screen.exitonclick()