##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv - DONE

# 2. Check if today matches a birthday in the birthdays.csv - DONE-ish

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



############# Step 1: Read the csv to comply with point #2

import pandas as pd
import datetime as dt

now = dt.datetime.now()
month = now.month
today = now.day
# print(f"Month: {month}, Day: {today}")


df = pd.read_csv("birthdays.csv")
bday = df[(df["month"] == month) & (df["day"] == today)]
if not bday.empty:
    print("True")
else:
    print("False")


############# Step 2: Follow point #3

from random import choice

letter = choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])

old_value = "[NAME]"
new_value = bday["name"]
print(new_value)

# with open(f"./letter_templates/{letter}", "w") as file:
#     letter = file.read()
#     letter = letter.replace("[NAME]", f"{df.name}")
    # print(letter)
    