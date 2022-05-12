import requests
from datetime import datetime
import smtplib
import time

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_positions = (iss_latitude, iss_longitude)

parameters =  {
    "lat" : 40.588711,
    "lng" : -73.940598,
    "formatted" : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    time.sleep(60)
    if parameters["lat"] - 5 <= iss_latitude <= parameters["lat"] + 5 and parameters["lng"] - 5 <= iss_longitude <= parameters["lng"] + 5:
        if sunset <= time_now.hour <= sunrise:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user="sdeveloper444@gmail.com", password="206480220aB")
            connection.sendmail(from_addr="sdeveloper444@gmail.com",
                                to_addrs="sdeveloper444@gmail.com",
                                msg="Subject: ISS above you👆🏼.\n\nLook up for the ISS!")


