from tkinter import *


def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=50, pady=50)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text", padx=20, pady=20)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=3)
input.get()


window.mainloop()

# Components of a GUI window
# Label = text displayed as information
# Button = button that will activate on a click, and can collect information or activate a function
# Entry = text box to record user input
# Text = multi-line text box to record user input
# Spinbox = display box with options to select one using arrow buttons
# Scale = draggable bar to select an option
# Checkbutton = small checkbox to select an option
# Radiobutton = similar to checkboxes, but rounded
# Listbox = text box with a list of strings
