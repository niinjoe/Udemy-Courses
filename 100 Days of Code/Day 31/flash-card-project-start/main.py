# Imports
from tkinter import *
from random import randint
import pandas as pd

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- READ CSV ------------------------------- #

df = pd.read_csv("./data/french_words.csv")
data = df.to_dict(orient="records")
selected_word = data[randint(0, len(data))]["French"]


# ---------------------------- UI SETUP ------------------------------- #

# Create GUI window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
# When appending the desired image to the class, use half the size in pixels to center it
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
canvas.create_text(400, 150, text="test_lang", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text=selected_word, font=("Arial", 60, "bold"))

# Buttons
right_button = Button(image=right, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(row=1, column=1)

window.mainloop()