from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    # count_down(5*60)
    global reps
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60

    #If its the 1st,3rd,5th,7th rep:
    if reps == 0:
      count_down(work_sec)
      reps = 1
    #If its the 8th rep:
    # count_down(long_break_sec)
    #If its 2nd,4th,6th rep:
    # count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(
    102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# Labels
timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
timer.grid(column=1, row=0)

checkmarks = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmarks.grid(column=1, row=3)

# Buttons
start = Button(text="Start", command=timer_start)
start.grid(column=0, row=2)

reset = Button(text="Reset")
reset.grid(column=2, row=2)


window.mainloop()
