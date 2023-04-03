from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels
timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
timer.grid(column=1, row=0)

checkmarks = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmarks.grid(column=1, row=3)

# Buttons
start = Button(text="Start")
start.grid(column=0, row=2)

reset = Button(text="Reset")
reset.grid(column=2, row=2)



window.mainloop()
