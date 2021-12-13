from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

def reset_game(l_paddle, r_paddle, ball):
    l_paddle.goto(-350, 0)
    r_paddle.goto(350, 0)
    ball.goto(0, 0)
    time.sleep(2)


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.tracer(0)
    screen.title("Pong")
    screen.bgcolor("black")

    l_paddle = Paddle((-350, 0))
    l_paddle.configure_listeners(screen, up="w", down="s")

    r_paddle = Paddle((350, 0))
    r_paddle.configure_listeners(screen, up="Up", down="Down")

    ball = Ball()

    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()

        if ball.ycor() >= 290 or ball.ycor() <= -290:
            ball.bounce()

        if ball.xcor() >= 340 and r_paddle.distance(ball) < 50:
            print("Collision with right paddle!")
            ball.paddle_bounce()

        if ball.xcor() <= -340 and l_paddle.distance(ball) < 50:
            print("Collision with left paddle!")
            ball.paddle_bounce()

        if ball.xcor() > 360:
            print("Player 1 scores!")
            reset_game(l_paddle, r_paddle,ball)
        elif ball.xcor() <= -360:
            print("PLayer 2 scores!")
            reset_game(l_paddle,r_paddle,ball)

    screen.exitonclick()
