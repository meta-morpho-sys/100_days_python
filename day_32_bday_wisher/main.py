##################### App for Sending of Birthday Emails  ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
#################################################################################

import datetime as dt
import os
import random
import smtplib
import pandas as pd


today = dt.date.today()
year = today.year
SENDER_EMAIL = "yuliya.nedyalkova777@gmail.com"
PASSWORD = os.getenv('GMAIL_SERVICE_PASS')


# ------------------------------ PREP DATA ------------------------------ #
birthdays = pd.read_csv('birthdays.csv')
birthdays_dict = birthdays.to_dict(orient="records")

# ------------------------------ CHECK IF IT IS SOMEONE'S BIRTHDAY ------------------------------ #
def birthday_check():
    global name
    for entry in birthdays_dict:
        name = entry['name']
        email = entry['email']
        month = entry['month']
        day = entry['day']
        birthday = dt.date(year=year, month=month, day=day)
        if birthday == today:
            print(f"Wooohoo!! Today is the {today} and it's {name}'s birthday!!")
            bday_msg = write_message(name)
            send_bday_email(email, bday_msg)
            print(f"Email to {name} was sent")


# ------------------------------ PREP BIRTHDAY MESSAGE ------------------------------ #
def write_message(bday_person):
    templates = os.listdir('letter_templates')
    template = random.choice(templates)

    with open(f"letter_templates/{template}") as template_text:
        text = template_text.read()

    letters_dir = 'ready_letters'
    if not os.path.exists(letters_dir):
        os.makedirs(letters_dir)
    if not os.path.exists(f"{letters_dir}/{year}"):
        os.makedirs(f"{letters_dir}/{year}")
    else:
        with open(f"{letters_dir}/{year}/{bday_person}_b_day", 'w') as bday_letter:
            new_text = text.replace('[NAME]', bday_person)
            bday_letter.write(new_text)
        return new_text


# ------------------------------ SEND BIRTHDAY EMAIL ------------------------------ #
def send_bday_email(addressee, msg):
    with smtplib.SMTP('smtp.gmail.com') as conn:
        conn.starttls()
        conn.login(SENDER_EMAIL, PASSWORD)
        conn.sendmail(SENDER_EMAIL, addressee, f"Subject: Test for birthday greetings email\n\n{msg}")
        conn.close()


birthday_check()


