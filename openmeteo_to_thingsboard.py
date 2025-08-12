import requests
import os

# Dein Access Token aus ThingsBoard
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]

# Open-Meteo API Parameter (Current Weather)
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 50.5441,
    "longitude": 9.6811,
    "current": "temperature_2m,relative_humidity_2m,rain,wind_speed_10m,wind_direction_10m,snowfall,showers",
    "timezone": "Europe/Berlin"
}

# 1. Wetterdaten abrufen
weather = requests.get(url, params=params).json()

# 2. Werte aus dem "current"-Block lesen
current_data = weather["current"]

payload = {
    "temperature": current_data.get("temperature_2m"),
    "humidity": current_data.get("relative_humidity_2m"),
    "rain": current_data.get("rain"),
    "wind_speed": current_data.get("wind_speed_10m"),
    "wind_direction": current_data.get("wind_direction_10m"),
    "snowfall": current_data.get("snowfall"),
    "showers": current_data.get("showers")
}

# 3. An ThingsBoard senden
thingsboard_url = f"https://iot-demo.bda-itnovum.com/api/v1/{ACCESS_TOKEN}/telemetry"
response = requests.post(thingsboard_url, json=payload)

print("Status:", response.status_code)
print("Antwort:", response.text)
