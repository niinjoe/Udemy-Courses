from tkinter import *

def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()

# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
print(input.get())
input.pack()



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