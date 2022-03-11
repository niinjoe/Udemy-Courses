from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f" {self.l_score} | {self.r_score} ", align=ALIGNMENT, font=FONT)
        if self.l_score == 10:
            self.clear()
            self.write(f"Left Player Wins!", align=ALIGNMENT, font=FONT)
        elif self.r_score == 10:
            self.clear()
            self.write(f"Right Player Wins!", align=ALIGNMENT, font=FONT)
        else:
            pass

    def l_collect(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_collect(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
