import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.mainloop()

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
