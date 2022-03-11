from turtle import Screen, Turtle
from random import choice

tm = Turtle()

colors = [
    "black",
    "deep sky blue",
    "cadet blue",
    "forest green",
    "aquamarine",
    "dark olive green",
    "orange",
    "firebrick",
    "maroon",
    "gold",
    "cornflower blue",
    "dark goldenrod",
    "orange red",
    "rosy brown",
    "purple",
    "orchid",
    "pale violet red",
    "medium purple",
    "slate blue",
    "dark gray",
    "slate gray",
    "midnight blue",
]

tm.speed("fastest")
x = 3
c = True
while c:
    for _ in range(x):
        tm.fd(40)
        tm.right(360 / x)
    tm.pencolor(choice(colors))
    x += 1
    # if x > 10:
    #     c = False

screen = Screen()
screen.exitonclick()

import heroes

print(heroes.gen())
