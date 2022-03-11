from turtle import Turtle, Screen
from tkinter import messagebox
import random

sc = Screen()

sc.setup(width=500, height=400)
sc.title("Welcome to the turtle death race!")
user_bet = sc.textinput(
    "Make your bet!",
    "Which turtle will arrive first? (red, orange, yellow, green, blue or purple): ",
).lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-125, -75, -25, 25, 75, 125]
turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_pos[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_dist = random.randint(0, 10)
        turtle.fd(rand_dist)
        if turtle.xcor() > 230:
            is_race_on = False
            victorious_color = turtle.pencolor()
            if victorious_color == user_bet:
                messagebox.showinfo(
                    "Result",
                    f"You've won!\nThe {victorious_color} turtle arrived first!",
                )
            else:
                messagebox.showinfo(
                    "Result",
                    f"You've lost!\nThe {victorious_color} turtle arrived first!",
                )


sc.exitonclick()
