import requests
from datetime import datetime
import os
import smtplib


MY_LAT = 51.789018
MY_LONG = -1.484935
# VARNA_LAT = 43.214050
# VARNA_LONG = 27.914734


sender_username = 'yuliya.nedyalkova777@gmail.com'
sender_password = os.getenv('BDAY_WISHER_PASS')
weather_api_key = os.getenv('OPEN_WEATHER_API_KEY')


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()


def is_iss_near():
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_coordinates = (iss_latitude, iss_longitude)

    #Your position is within +5 or -5 degrees of the ISS position.
    positive_offset = 5
    negative_offset = -5

    if MY_LAT + positive_offset >= iss_latitude >= MY_LAT + negative_offset and MY_LONG + positive_offset >= iss_longitude >= MY_LONG + negative_offset:
        print('ISS is close!')
        print(f"ISS is in {iss_coordinates}")
        return True
    else:
        print('ISS is out of range!')
        print(f"ISS is in {iss_coordinates}")
        return False

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_position_data = response.json()
    time_now = datetime.now()
    current_hour = time_now.hour

    sunrise = int(sun_position_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_position_data["results"]["sunset"].split("T")[1].split(":")[0])

    if sunrise > current_hour > sunset:
        print("It's dark")
        return True
    else:
        print("It's daylight")
        return  False

def is_clear_skies():
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LONG}&appid={weather_api_key}&units=metric")
    data = weather_response.json()
    weather_state = data['weather'][0]['description']
    if 'few clouds'or 'clear sky' in weather_state:
        print(weather_state)
        return True
    else:
        print(f"The weather is: {weather_state}")
        return False


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(sender_username, sender_password)
        conn.sendmail(sender_username,sender_username, "Subject:\n\n Yuliya ISS is near. Look up now!!!")
        print("email sent")
        conn.close()


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

if is_clear_skies() and is_dark():
    if is_iss_near():
        send_mail()

# BONUS: run the code every 60 seconds.


