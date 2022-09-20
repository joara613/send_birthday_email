import smtplib
import random
import datetime as dt
import pandas as pd


MY_EMAIL = "calgaryprogramming91@gmail.com"
MY_PASSWORD = "password"

now = dt.datetime.now()
month = now.month
day = now.day


bd_df = pd.read_csv("birthdays.csv")
for index, row in bd_df.iterrows():
    if row["month"] == month and row["day"] == day:

        receiver = row["name"]
        letter_num = random.randint(1, 3)

        with open(f"./letter_templates/letter_{letter_num}.txt") as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", receiver)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday!\n\n{letter}")
        print(f"A birthday email was sent to {receiver} at {now.time()}")