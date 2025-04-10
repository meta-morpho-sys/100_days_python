##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import os
import random
import pandas as pd

name = ''
today = dt.date.today()
year = today.year

# ------------------------------ PREP DATA ------------------------------ #
birthdays = pd.read_csv('birthdays.csv')
birthdays_dict = birthdays.to_dict(orient="records")

# ------------------------------ CHECK IF IT IS SOMEONE'S BIRTHDAY ------------------------------ #
def birthday_check():
    global name
    for entry in birthdays_dict:
        name = entry['name']
        month = entry['month']
        day = entry['day']
        birthday = dt.date(year=year, month=month, day=day)
        if birthday == today:
            print(f"Wooohoo!! It's {name}'s birthday today the {birthday}")
        return birthday, name, year


# ------------------------------ PREP BIRTHDAY MESSAGE ------------------------------ #
def write_message():
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
        with open(f"{letters_dir}/{year}/{name}_b_day", 'w') as bday_letter:
            new_text = text.replace('[NAME]', name)
            bday_letter.write(new_text)



# ------------------------------ SEND BIRTHDAY EMAIL ------------------------------ #



birthday_check()
write_message()

