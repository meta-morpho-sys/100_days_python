# 👩‍🚀 ISS Tracker and Notifier

This Python script checks if the International Space Station (ISS) is currently flying over your location **at night and during clear skies** — and notifies you via email when the conditions are just right to observe it. It also plots the current ISS location on a live map using Folium.

---

## 🚀 Features

- 🔭 Tracks the real-time position of the ISS.
- 🌙 Checks if it's currently dark at your location.
- 🌤️ Evaluates if the weather is clear (ideal for viewing the ISS).
- 🗺️ Plots the current ISS location on a live-updating map (`current_location.html`).
- 📧 Sends you an email notification when the ISS is visible from your location.

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install requests folium
🔧 Environment Variables
Before running the script, set the following environment variables:

Variable Name	Description
GMAIL_SERVICE_PASS	Your Gmail App Password (not your main password)
OPEN_WEATHER_API_KEY	API key from OpenWeatherMap
📍 Configuration
Update these constants and variables in the script to your own coordinates:

python
Copy
Edit
MY_LAT = 51.789018       # Your latitude
MY_LONG = -1.484935      # Your longitude
sender_username = "your_email@example.com" The username of the account (gmail, hotmail, etc) from and to which the email will be sent out. (At the moment the program is used to send an email to yourself)
📤 How to Use
Just run the script:

bash
Copy
Edit
python iss_tracker.py
The script will:

Check if the ISS is within ~5 degrees of your location.

Ensure it's nighttime.

Check if the sky is clear.

If all checks pass, it sends you an email.

Every 60 seconds, it updates the ISS location on a map (current_location.html).

📧 Email Notification Setup
You need to enable "App Passwords" on your Gmail account:

Enable 2FA for your Google account.

Generate an App Password from Google Account > Security > App passwords.

Use this password in the GMAIL_SERVICE_PASS environment variable.

🛑 Stop the Script
The script runs indefinitely. Use CTRL+C in the terminal to stop it.

🗺️ Output
current_location.html – A browser-viewable map showing the current location of the ISS.

🧠 Future Ideas
Add Slack or SMS notifications.

Display ISS trajectory or trail.

Deploy as a web dashboard with Flask or Dash.

Made with 🌍 and 🚀 by Yuliya.