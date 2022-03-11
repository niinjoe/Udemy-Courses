from turtle import Screen, Turtle
from random import choice, randint
import turtle as t

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

directions = [0, 90, 180, 270]

# tuples:
t.colormode(255)
rgb = (1, 3, 8)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


tm.pensize(15)
tm.speed("fastest")

for _ in range(300):
    tm.color(random_color())
    tm.fd(30)
    tm.setheading(choice(directions))

screen = Screen()
screen.exitonclick()
