import requests
import time
from datetime import datetime

MY_LAT = 53.349804
MY_LONG = -6.260310

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.

def is_iss_nearby(iss_location):
    if MY_LAT-5 <= iss_location[0] <= MY_LAT+5:
        if MY_LONG-5 <= iss_location[1] <= MY_LONG+5:
            return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    # If the ISS is close to my current position
    if is_iss_nearby((iss_latitude, iss_longitude)):
        if time_now.hour > sunset or time_now.hour < sunrise:
            print("look up! ISS is nearby!")
        else:
            print("Not dark, but the ISS is nearby!")
    else:
        print("The ISS is not nearby")
    time.sleep(60)

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
