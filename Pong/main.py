from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def reset_game(l_paddle, r_paddle, ball):
    l_paddle.goto(-350, 0)
    r_paddle.goto(350, 0)
    ball.reset()
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

    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.xcor() > 350:
            scoreboard.l_point()
            reset_game(l_paddle, r_paddle, ball)
            ball.paddle_bounce()
        elif ball.xcor() <= -350:
            scoreboard.r_point()
            reset_game(l_paddle, r_paddle, ball)
            ball.paddle_bounce()

        if ball.ycor() >= 290 or ball.ycor() <= -290:
            ball.bounce()

        if ball.xcor() >= 330 and r_paddle.distance(ball) < 50:
            print("Collision with right paddle!")
            ball.paddle_bounce()

        if ball.xcor() <= -330 and l_paddle.distance(ball) < 50:
            print("Collision with left paddle!")
            ball.paddle_bounce()

    screen.exitonclick()
