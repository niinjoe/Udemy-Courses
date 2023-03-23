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
results = []
count = len(results)

while game_on:
    answer_state = screen.textinput(
        title=f"{count}/50 States Correct", prompt="Give me a state name."
    ).title()

    # if answer_state is not None:
    #     answer_state = answer_state.title()
    #     print(answer_state)
    # else:
    #     print("User clicked Cancel.")

    result_row = df.loc[df["state"] == answer_state]
    # results.append(answer_state)

    states_list = df["states"].tolist()
    if answer_state in states_list:
        results.append(answer_state)

    if not result_row.empty:
        x_cor = result_row["x"].iloc[0]
        y_cor = result_row["y"].iloc[0]

    my_turtle.penup()
    my_turtle.goto(x_cor, y_cor)
    my_turtle.write(answer_state)


print(results)
