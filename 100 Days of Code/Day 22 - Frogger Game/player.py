from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.left(90)
        self.penup()
        self.finish()
        self.shape("turtle")
        self.color("green")

    def up(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        self.goto(STARTING_POSITION)
