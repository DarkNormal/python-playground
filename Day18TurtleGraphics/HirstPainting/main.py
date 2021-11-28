from color_importer import ColorImporter
import turtle as t
import random


def random_color(colors):
    return colors[random.randint(0, len(colors)-1)]


if __name__ == '__main__':
    color_importer = ColorImporter()
    colors = color_importer.import_colors("image.jpeg")

    turtle = t.Turtle()
    turtle.penup()
    turtle.setx(-300)
    turtle.sety(-250)
    turtle.speed(0)
    turtle.hideturtle()

    t.colormode(255)

    for _ in range(10):
        for _ in range(10):
            turtle.penup()
            turtle.forward(50)
            color = random_color(colors)
            turtle.color(color)
            turtle.pendown()
            turtle.fillcolor(color)
            turtle.begin_fill()
            turtle.dot(20, color)
            turtle.end_fill()
        #move turtle up to next row
        turtle.penup()
        turtle.setx(-300)
        turtle.sety(turtle.ycor() + 50)

    screen = t.Screen()
    screen.exitonclick()
