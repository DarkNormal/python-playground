import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()

screen.listen()
screen.onkeypress(key="Up", fun=player1.move)


def next_level():
    pass
    # TODO speed up cars


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player1.is_finished():
        next_level()
