from tkinter import *
from tkinter import messagebox
import csv
import os.path
from random import *
import pyperclip
import string
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    # Create character lists for letters, numbres and symbols
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    numbers = [str(num) for num in list(range(0, 10))]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    # Loop through lists to select ammount of characters randomly
    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Create a new list containing all characters previosly selected, shuffle them & join together to a string
    password_list = pw_letters + pw_numbers + pw_symbols
    shuffle(password_list)
    password = "".join(password_list)

    # On command fill the entrybox when button press active and copy to clipboard automatically
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE/FIND PASSWORD ------------------------------- #


def save():

    # Define variables to get strings
    website = website_entry.get()
    account = account_entry.get()
    password = password_entry.get()
    # Define initial json structure with a dictionary
    new_data = {
        website: {
            "email": account,
            "password": password,
        }
    }

    # Validate no box is left empty before saving to json
    if len(website) == 0 or len(account) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="No field should be left blank.")
    else:
        # Try is used to run a line of code that could give an error (in this case, it will give an error if the file doesn't exist)
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        # The exception will execute if no file is found and create the new file so we don't get an error code
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Creating new json file
                json.dump(new_data, file, indent=4)
        # Else will execute once try or exception run
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        # Finally will alwyas clear entries no matter what happens with the rest of the conditions
        finally:
            # Clear entries after button press
            website_entry.delete(0, END)
            account_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    # Again, we try a line of code that could result in an error
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    # If the above code fails, it will probably be due to a file missing, so we execute the exception
    except FileNotFoundError:
        messagebox.showerror(
            title="Error", message="Database is missing or not created."
        )
    # Else will execute last once the try or except are executed
    else:
        # We create a condition to figure out if the input is available in the json file
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=f"{website}", message=f"Email: {email}\nPassword: {password}"
            )
            pyperclip.copy(password)
        else:
            messagebox.showerror(
                title="Not found",
                message="The value provided is non-existent in this database.",
            )


# ---------------------------- UI SETUP ------------------------------- #

# Create GUI window
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
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()

account_entry = Entry(width=50)
account_entry.grid(row=2, column=1, columnspan=2)
account_entry.insert(0, "@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generator)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=48, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

# Keep window open
window.mainloop()
