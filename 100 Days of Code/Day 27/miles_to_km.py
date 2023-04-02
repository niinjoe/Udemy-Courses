from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(300, 200)
window.config(padx=10, pady=10)


# 1 mile = 1.6 Km
def button_clicked():
    new_text = input.get()
    conversion = float(new_text) * 1.6
    result.config(text=round(conversion, 1))


# input/entry
input = Entry(width=10)
input.grid(column=1, row=0)

# labels
miles = Label(width=10, text="Miles")
miles.grid(column=2, row=0)

equal = Label(width=10, text="is equal to:")
equal.grid(column=0, row=1)

result = Label(width=10)
result.grid(column=1, row=1)

km = Label(width=10, text="Km")
km.grid(column=2, row=1)

# button
calc_butt = Button(width=10, text="Calculate", command=button_clicked)
calc_butt.grid(column=1, row=3)


window.mainloop()
