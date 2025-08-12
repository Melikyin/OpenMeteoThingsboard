import requests
from datetime import datetime
import os

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]  # Holt Token aus GitHub Secret

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m,rain,wind_speed_80m,wind_direction_80m,relative_humidity_2m",
    "timezone": "auto"
}

weather = requests.get(url, params=params).json()

temp = weather["hourly"]["temperature_2m"][0]
rain = weather["hourly"]["rain"][0]
wind_speed = weather["hourly"]["wind_speed_80m"][0]
wind_dir = weather["hourly"]["wind_direction_80m"][0]
humidity = weather["hourly"]["relative_humidity_2m"][0]

thingsboard_url = f"https://iot-demo.bda-itnovum.com/api/v1/{ACCESS_TOKEN}/telemetry"
payload = {
    "temperature": temp,
    "rain": rain,
    "wind_speed": wind_speed,
    "wind_direction": wind_dir,
    "humidity": humidity,
    "timestamp": datetime.now().isoformat()
}

response = requests.post(thingsboard_url, json=payload)
print("Status:", response.status_code, "Antwort:", response.text)
