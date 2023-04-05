from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)

account = Label(text="Email/Username:")
account.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Entry
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

account_entry = Entry(width=40)
account_entry.grid(row=2, column=1, columnspan=2)
account_entry.insert(0, "@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()


# window = Tk()
# r = Label(bg="red", width=20, height=5)
# r.grid(row=0, column=0)

# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)

# b = Label(bg="blue", width=20, height=5)
# b.grid(row=2, column=0, columnspan=2)


# window.mainloop()
