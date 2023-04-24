##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv - DONE

# 2. Check if today matches a birthday in the birthdays.csv - DONE

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv - DONE

# 4. Send the letter generated in step 3 to that person's email address.



############# Step 1: Read the csv to comply with point #2

import pandas as pd
import datetime as dt

now = dt.datetime.now()
month = now.month
today = now.day

df = pd.read_csv("birthdays.csv")
bday = df[(df["month"] == month) & (df["day"] == today)]
if not bday.empty:
    bday_person = bday.iloc[0]["name"]
else:
    print("No birthdays today.")

############# Step 2: Follow point #3

from random import choice

letter = choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])

with open(f"./letter_templates/{letter}") as file:
    letter = file.read()
    letter = letter.replace("[NAME]", bday_person)
    # print(letter)
    
############# Final Step: Send message via email

import smtplib

# my_email = "ed.serrano.test@gmail.com"  # This is the sender email
my_email = "daftsapien@gmail.com"  # This is the sender email
# password = "maerzcuqgyrrjedd"  # This is the app password, not the account password (for google)
password = "vmigvmepcdghnnqj"  # This is the app password, not the account password (for google)
test_email = "joe_serrano_test@yahoo.com"  # This is the receivers email

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=test_email,
        msg=f"Subject:Happy Birthday!\n\n{letter}",
        )