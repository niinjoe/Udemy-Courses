from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class GameMenu(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 100)
        self.hideturtle()
        self.pencolor("white")

    def menu(self):
        self.write(f"Welcome to Nokia Snake", align=ALIGNMENT, font=FONT)

    def select_option(self):
        self.goto(0, 50)
        self.write(f"Start Game", align=ALIGNMENT, font=FONT)
