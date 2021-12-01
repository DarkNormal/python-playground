from turtle import Turtle, Screen
import random

def draw_finish_line():
    t = Turtle()
    t.penup()
    t.setx(230)
    t.sety(200)
    t.right(90)
    t.pensize(5)
    for _ in range(16):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(15)
    #turn turtle around to do the second dashed line to look like a finish line
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(2)
    for _ in range(20):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(15)


is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)

draw_finish_line()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue"]
turtles=[]
ycoord = -100
for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=ycoord)
    turtles.append(t)
    ycoord += 50

if user_bet in colors:
    is_game_on = True

while is_game_on:
    for turtle in turtles:
        random_movement = random.randint(1, 15)
        turtle.forward(random_movement)
        if turtle.xcor() >= 230:
            print(f"Turtle {turtle.color()} is the winner!")
            is_game_on = False
            if user_bet == turtle.color():
                print("You were right!")
            else:
                print("You lost your bet..")


screen.exitonclick()
