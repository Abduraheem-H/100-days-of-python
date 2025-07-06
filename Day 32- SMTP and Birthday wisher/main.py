import pandas
import smtplib
import random
import datetime as dt
import os


MY_PASSWPORD = os.getenv(
    "MY_PASSWPORD"
)  # Set this environment variable outside your code


today = dt.datetime.now()

csv = pandas.read_csv("./birthdays.csv")

for index, row in csv.iterrows():
    if today.month == row["month"] and today.day == row["day"]:
        letter = f"letter_{random.randint(1,3)}.txt"
        with open(f"./letter_templates/{letter}", "r") as letter_file:
            message = letter_file.read().replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com") as server:
            server.starttls()
            server.login(user=row["email"], password=MY_PASSWPORD)
            server.sendmail(
                from_addr=row["email"],
                to_addrs=row["email"],
                msg=f"Subject: Happy Birth Day\n\n {message}",
            )
    print(
        f"Birth day notification email sent to {row['name']} to their email address: {row['email']}"
    )
