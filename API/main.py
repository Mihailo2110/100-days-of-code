import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "mihailomilovanovic21@gmail.com"
PASSWORD = "kscole12gmailcom"
MY_LAT = 44.016521
MY_LNG = 21.005859

def above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LNG - 5 < iss_longitude < MY_LNG + 5:
        return True

def dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now > sunset or time_now < sunrise:
        return True

while True:
    time.sleep(60)
    if above() and dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:ISS!\n\nLOOK UP!.")


