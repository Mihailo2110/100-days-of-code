import requests
import smtplib

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "95569f732e4ba00ec846c7a7072917b7"

weather_params = {
    "lat": 44.016521,
    "lon": 21.005859,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

condition_codes = []
position = 0
for i in range(0, 12):
    condition_codes.append(weather_data["hourly"][position]["weather"][0]["id"])
    position += 1

for i in condition_codes:
    if i < 700:
        print("bring umbrella!")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="mihailomilovanovic21@gmail.com", password="kscole12gmailcom")
            connection.sendmail(from_addr="mihailomilovanovic21@gmail.com", to_addrs="mihailomilovanovic21@gmail.com", msg=f"Subject:VREME\n\nPonesi kisobran!")
        break


