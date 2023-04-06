from tkinter import *
from tkinter import messagebox
import csv
import os.path
from random import *
import pyperclip
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    numbers = [str(num) for num in list(range(0, 10))]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = pw_letters + pw_numbers + pw_symbols

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

headers = ["Website", "Email/Username", "Password"]


def save():

    # Define variables to get strings
    website = website_entry.get()
    account = account_entry.get()
    password = password_entry.get()

    # Validate no box is left empty before saving to csv
    if len(website) == 0 or len(account) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="No field should be left blank.")
    else:
        # Confirm credentials were entered correctly
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail:{account}\nPassword:{password}\nIs it OK to save?",
        )

        if is_ok:
            if not os.path.isfile("data.csv"):
                # If the file doesn't exist, create it and write the headers
                with open("data.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)

            # Append new rows to the file without writing headers
            with open("data.csv", "a", newline="") as file:
                writer = csv.writer(file)
                # Write new rows as lists of values
                writer.writerow(
                    [
                        f"{website}",
                        f"{account}",
                        f"{password}",
                    ]
                )

            # Clear entries after button press
            website_entry.delete(0, END)
            account_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pass Password Manager")
window.config(padx=40, pady=40)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

account_label = Label(text="Email/Username:")
account_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

account_entry = Entry(width=50)
account_entry.grid(row=2, column=1, columnspan=2)
account_entry.insert(0, "@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generator)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
