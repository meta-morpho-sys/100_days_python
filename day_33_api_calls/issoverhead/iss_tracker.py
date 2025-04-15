import logging as log
import time

import requests
from datetime import datetime
import os
import smtplib
import folium
import subprocess
from pathlib import Path

MY_LAT = 51.789018
MY_LONG = -1.484935
THIS_FOLDER = Path(__file__).parent.resolve()



sender_username = 'yuliya.nedyalkova777@gmail.com'
sender_password = os.getenv('GMAIL_SERVICE_PASS')
weather_api_key = os.getenv('OPEN_WEATHER_API_KEY')

log.basicConfig(level=log.INFO, format="[%(levelname)s : %(asctime)s] %(message)s")


def is_iss_near():
    log.info("Checking if ISS is near")
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_coordinates = (iss_latitude, iss_longitude)

    #Your position is within +5 or -5 degrees of the ISS position.
    positive_offset = 5
    negative_offset = -5

    if MY_LAT + positive_offset >= iss_latitude >= MY_LAT + negative_offset and MY_LONG + positive_offset >= iss_longitude >= MY_LONG + negative_offset:
        log.info(f'ISS is close! Coordinates: {iss_coordinates}')
        return True, iss_coordinates
    else:
        log.info(f'ISS is out of range!Coordinates: {iss_coordinates}')
        return False, iss_coordinates

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    log.info("Checking for nighttime")
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_position_data = response.json()
    time_now = datetime.now()
    current_hour = time_now.hour

    sunrise = int(sun_position_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_position_data["results"]["sunset"].split("T")[1].split(":")[0])


    if current_hour >= sunset or current_hour <= sunrise:
        log.info("It's dark")
        return True
    else:
        log.info("It's daylight")
        return  False

def is_clear_sky():
    log.info("Checking for sky conditions and visibility")
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LONG}&appid={weather_api_key}&units=metric")
    data = weather_response.json()
    current_weather_state = data['weather'][0]['description']
    if current_weather_state == 'few clouds' or current_weather_state == 'clear sky':
        log.info(f"Good weather today with {current_weather_state}")
        return True
    else:
        log.info(f"The weather is not good for observation: {current_weather_state}")
        return False

def plot_on_map():
    _, coordinates = is_iss_near()
    m = folium.Map(location=coordinates, zoom_start=4)
    folium.Marker(location=coordinates, popup="Current Location").add_to(m)
    m.save("current_location.html")
    my_plot_file = f"{THIS_FOLDER}/current_location.html"
    try: # should work on Windows
        os.startfile(my_plot_file)
    except AttributeError:
        try: # should work on MacOS and most linux versions
            subprocess.call(['open', my_plot_file])
        except:
            log.error('Could not open URL')

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(sender_username, sender_password)
        conn.sendmail(sender_username,sender_username, "Subject:\n\n Yuliya ISS is near. Look up now!!!")
        print("email sent")
        conn.close()

while True:
    plot_on_map()
    if is_iss_near() and is_dark():
        if is_clear_sky():
            send_mail()
    time.sleep(60)



