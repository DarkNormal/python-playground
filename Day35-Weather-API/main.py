import requests

WEATHER_URL = "https://api.openweathermap.org/data/2.5/onecall"
API_TOKEN = "REDACTED"
LATITUDE = "53.259950"
LONGITUDE = "-6.323910"
EXCLUDE = "current,minutely,daily"

parameters = {"lat": LATITUDE,
              "lon": LONGITUDE,
              "exclude": EXCLUDE,
              "appId": API_TOKEN}

result = requests.get(WEATHER_URL, params=parameters)
result.raise_for_status()
#print(result.json()["hourly"])
weatherNext12hours = result.json()["hourly"][:12]
for hourlyForecast in weatherNext12hours:
    hourlyCondition = hourlyForecast["weather"][0]["id"]
    print(hourlyCondition)
    if hourlyCondition < 700:
        print("You're gonna need an umbrella")
print(weatherNext12hours)


