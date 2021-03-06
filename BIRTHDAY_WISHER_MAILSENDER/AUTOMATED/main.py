import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "mihailomilovanovic21@gmail.com"
PASSWORD = "kscole12gmailcom"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    bithday_person = birthdays_dict[today]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bithday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=bithday_person.email, msg=f"Subject:Happy Birthday!\n\n{contents}.")



