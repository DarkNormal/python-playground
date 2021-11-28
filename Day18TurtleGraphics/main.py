import turtle as t
import random

colors = ["aquamarine", "DarkMagenta", "DarkOrange", "DeepPink", "DodgerBlue", "gold"]
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def random_walk(turtle):
    turtle.pensize(10)
    for _ in range(300):
        turtle.color(random_color())
        turtle.seth(random.choice(directions))
        turtle.forward(20)


def shapes_overlap(turtle):
    # Draw multiple shapes overlapping
    for num_sides in range(3, 9):
        angle = 360 / num_sides
        turtle.color(colors[num_sides - 3])
        for side in range(num_sides):
            turtle.forward(50)
            turtle.right(angle)

def spirograph(turtle):
    turtle.speed(0)
    for i in range(36):
        turtle.setheading(turtle.heading() + 10)
        turtle.circle(100)
        turtle.color(random_color())


tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("chartreuse")


for i in range(4):
    tim.forward(100)
    tim.right(90)

tim.reset()

for i in range(10):
    if i % 2 == 0:
        tim.pendown()
    else:
        tim.penup()
    tim.forward(10)
tim.reset()

#shapes_overlap(tim)
tim.reset()

#random_walk(tim)
tim.reset()

spirograph(tim)

screen = t.Screen()
screen.exitonclick()
