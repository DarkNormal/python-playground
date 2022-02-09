from turtle import Turtle

FONT = ("Arial", 16, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.hideturtle()
        self.goto(0, 275)
        self.color("white")
        self.write_score()

    def update_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.write_high_score()
            self.read_high_score()
        self.score = 0
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def read_high_score(self):
        with open(file="high_score.txt", mode="r") as high_score:
            self.high_score = int(str(high_score.read()))

    def write_high_score(self):
        with open(file="high_score.txt", mode="w") as high_score:
            high_score.write(str(self.score))
