import requests
import os


# Witney,UK
MY_LAT = 51.789018
MY_LONG = -1.484935
weather_api_key = os.getenv('OPEN_WEATHER_API_KEY')
weather_forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
condition_codes = []
params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': weather_api_key,
    'units': 'metric',
    'cnt': 4
}


# CHECK IF THE WEATHER FORCAST IS SUNNY
response = requests.get(weather_forecast_url, params=params)
response.raise_for_status()
twelve_hour_weather_data = response.json()
weather_forecast = twelve_hour_weather_data['list']
[condition_codes.append(forcast['weather'][0]['id']) for forcast in weather_forecast]


if any(code < 700 for code in condition_codes):
    print("No need to water the plants")
else:
    print("Water the plants")
