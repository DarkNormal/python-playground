import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()

score = Scoreboard()

carManager = CarManager()

screen.listen()
screen.onkeypress(key="Up", fun=player1.move)


def next_level():
    carManager.increment_difficulty()
    player1.reset()
    score.next_level()


def game_over():
    score.end_game()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_car()
    carManager.move_cars()
    carManager.check_cars()

    if player1.is_finished():
        next_level()
    elif carManager.detect_collision(player1):
        game_is_on = False
        game_over()

screen.exitonclick()
