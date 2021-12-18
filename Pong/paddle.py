from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coords):
        super().__init__()
        self.left(90)
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        #self.setx(coords[0])
        #self.sety(coords[1])
        self.setpos(coords)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)

    def configure_listeners(self, screen, up, down):
        screen.listen()

        screen.onkeypress(key=up, fun=self.move_up)
        screen.onkeypress(key=down, fun=self.move_down)
