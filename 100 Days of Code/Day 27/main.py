from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked.")

if button_clicked:
    my_label.config(text="I got clicked.")


button =  Button(text="Click Me", command=button_clicked)
button.pack()






window.mainloop()