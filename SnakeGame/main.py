from turtle import Screen
import time
from snake import Snake
from food import Food


if __name__ == '__main__':
    game_is_on = True
    screen = Screen()
    screen.tracer(0)
    screen.setup(width=500, height=500)
    screen.bgcolor("black")
    screen.title("Shnake game")

    snake = Snake()
    food = Food()

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
    screen.exitonclick()
