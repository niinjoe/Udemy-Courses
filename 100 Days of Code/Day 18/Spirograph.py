import turtle as t
import random as rd

tm = t.Turtle()

t.colormode(255)
tm.speed("fastest")


def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# for _ in range(36):
#     t.pencolor(random_color())
#     t.circle(75)
#     t.fd(1)
#     t.rt(10)


def draw(size):
    for _ in range(int(360 / size)):

        tm.pencolor(random_color())
        tm.setheading(tm.heading() + size)
        tm.circle(200)


draw(2)

screen = t.Screen()
screen.exitonclick()
