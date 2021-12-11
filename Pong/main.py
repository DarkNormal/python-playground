from turtle import Screen
from paddle import Paddle
from ball import Ball


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

    screen.exitonclick()
