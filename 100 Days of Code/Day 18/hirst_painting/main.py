# import colorgram as cl

# rgb_list = []

# colors = cl.extract('img.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_format = (r, g, b)
#     rgb_list.append(tuple_format)

# Generates this list:

color_list = [
    (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), 
    (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), 
    (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), 
    (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), 
    (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), 
    (65, 66, 56)
]

import turtle as tl
import random as rd
# dots have to be size 2, spaced by 50

tl.colormode(255)
t = tl.Turtle()
t.pensize(20)
t.hideturtle()

def move():
    for _ in range(10):
        t.dot(15, rd.choice(color_list))
        t.pu()
        t.fd(50)

def turn_right():
    t.rt(90), t.fd(50), t.rt(90), t.fd(50)

def turn_left():
    t.lt(90), t.fd(50), t.lt(90), t.fd(50)

t.pu()
t.setposition(-250, 250)

for _ in range(5):
    move()
    turn_right()
    move()
    turn_left()

screen = tl.Screen()
screen.exitonclick()
