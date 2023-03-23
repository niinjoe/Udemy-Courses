import turtle
import pandas as pd

df = pd.read_csv("50_states.csv")
my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_on = True

while game_on:
    answer_state = screen.textinput(
        title="Guess the State", prompt="Give me a state name."
    )

    result_row = df.loc[df["state"] == answer_state]

    if not result_row.empty:
        x_cor = result_row["x"].iloc[0]
        y_cor = result_row["y"].iloc[0]

    my_turtle.penup()
    my_turtle.goto(x_cor, y_cor)
    my_turtle.write(answer_state)


# turtle.mainloop()
