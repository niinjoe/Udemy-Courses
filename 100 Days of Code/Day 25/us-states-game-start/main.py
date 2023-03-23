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
results = df["state"].tolist()

while game_on:
    states_list = df["state"].tolist()
    count = len(results)

    if count == 50:
        answer_state = screen.textinput(
            title="Game completed.",
            prompt="Press Q to quit or S to start again.",
        ).title()
        if answer_state == "Q":
            break
        elif answer_state == "S":
            results = []
            count = 0
        else:
            answer_state = screen.textinput(
                title=f"{count}/50 States Correct",
                prompt="Invalid option. Press Q to quit or S to start again.",
            ).title()

    answer_state = screen.textinput(
        title=f"{count}/50 States Correct", prompt="Give me a state name."
    ).title()

    if answer_state in states_list:
        result_row = df.loc[df["state"] == answer_state]
        if not result_row.empty:
            x_cor = result_row["x"].iloc[0]
            y_cor = result_row["y"].iloc[0]

        my_turtle.penup()
        my_turtle.goto(x_cor, y_cor)
        my_turtle.write(answer_state)
        results.append(answer_state)

    while answer_state not in states_list:
        answer_state = screen.textinput(
            title=f"{count}/50 States Correct",
            prompt="Invalid answer. Please try again.",
        ).title()
        if answer_state in states_list:
            result_row = df.loc[df["state"] == answer_state]
            results.append(answer_state)

            if not result_row.empty:
                x_cor = result_row["x"].iloc[0]
                y_cor = result_row["y"].iloc[0]

            my_turtle.penup()
            my_turtle.goto(x_cor, y_cor)
            my_turtle.write(answer_state)
