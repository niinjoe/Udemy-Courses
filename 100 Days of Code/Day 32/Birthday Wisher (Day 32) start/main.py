import smtplib
import datetime as dt
import random as rd

# ------------------ Date Section
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(day_of_week)
# dob = dt.datetime(year=1990, month=12, day=21)
# print(dob)

# ------------------ File Section
with open("quotes.txt") as file:
    quotes = file.readlines()
# print(quotes)
quote_of_today = rd.choice(quotes)
# print(quote_of_today)

# ------------------ Email Section
my_email = "ed.serrano.test@gmail.com"  # This is the sender email
password = "pvdlhdrvdpesxqbd"  # This is the app password, not the account password (for google)
test_email = "joe_serrano_test@yahoo.com"  # This is the receivers email

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=test_email,
        msg=f"Subject:Hello\n\n{quote_of_today}",
    )
