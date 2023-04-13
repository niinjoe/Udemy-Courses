# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from random import randint, choice
import pandas as pd

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
current_card = None
# countdown = 3000

# ---------------------------- READ CSV ------------------------------- #

try:
    df = pd.read_csv("./data/words_to_learn.csv")
    data = df.to_dict(orient="records")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
    data = df.to_dict(orient="records")

# ----------This code is bugged when you call next_card() multiple times-------- #
# def flip_card_front():
#     canvas.itemconfig(card, image=card_front)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"], fill="black")

# def update_countdown():
#     global countdown
#     if countdown > 0:
#         countdown -= 1000
#         window.after(countdown, update_countdown)
#         flip_card_front()
#     else:
#         countdown = 3000
#     if countdown == 0:    
#         flip_card_back()

def flip_card_back():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_timer = window.after(3000, func=flip_card_back)
    # update_countdown()

def to_learn():
    data.remove(current_card)
    words_to_learn = pd.DataFrame(data)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

# Create GUI window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card_back)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
# When appending the desired image to the class, use half the size in pixels to center it
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
card_title = canvas.create_text(400, 150, fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, fill="black", font=("Arial", 60, "bold"))

# Buttons
right_button = Button(image=right, highlightthickness=0, command=to_learn)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()
print(current_card)
window.mainloop()
