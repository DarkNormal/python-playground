import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


if __name__ == '__main__':
    game_is_on = True
    screen = Screen()
    screen.tracer(0)
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Shnake game")

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(key="w", fun=snake.up)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="s", fun=snake.down)
    screen.onkey(key="d", fun=snake.right)

    screen.update()

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) <= 15:
            food.refresh()
            snake.grow()
            scoreboard.update_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

    screen.exitonclick()
