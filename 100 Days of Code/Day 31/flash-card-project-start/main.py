# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from random import randint, choice
import pandas as pd

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
countdown = 3000

# ---------------------------- READ CSV ------------------------------- #

df = pd.read_csv("./data/french_words.csv")
data = df.to_dict(orient="records")
# n = 0
# word_fr = ""
# word_en = ""

# def rand_num():
#     global n, word_en, word_fr
#     n = randint(0, len(data))
#     word_fr = data[n]["French"]
#     word_en = data[n]["English"]

# def change_word():
#     global current_word
#     rand_num()
#     canvas.delete(current_word)
#     current_word = canvas.create_text(400, 263, text=word_fr, font=("Arial", 60, "bold"))

def flip_card_back():
    canvas.itemconfig(card, image=card_back)

def flip_card_front():
    canvas.itemconfig(card, image=card_front)

def update_countdown():
    global countdown
    countdown -= 1000
    if countdown > 0:
        window.after(countdown, update_countdown)
    else:
        countdown = 0
        flip_card_back()

def next_card():
    current_card = choice(data)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    update_countdown()
    global countdown
    if countdown == 0:
        canvas.itemconfig(card_title, text="English")
        canvas.itemconfig(card_word, text=current_card["English"])
        countdown = 3000
        flip_card_front()



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
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))

# Buttons
right_button = Button(image=right, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
