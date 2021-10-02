import smtplib
import datetime as dt
import random

MY_EMAIL = "mihailomilovanovic21@gmail.com"
PASSWORD = "kscole12gmailcom"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 3:
   with open("quotes.txt", "r")as data:
        quotes_list = data.readlines()
        stiripped_quotes = [quote.strip("\n") for quote in quotes_list]
        quote = random.choice(stiripped_quotes)

   with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="katarina.stojanovic@henkel.com", msg=f"Subject:Hello\n\n{quote}.")
        print(quote)


