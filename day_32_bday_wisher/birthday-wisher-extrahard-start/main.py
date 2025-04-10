##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as pd

today = dt.date.today()

# ------------------------------ PREP DATA ------------------------------ #
birthdays = pd.read_csv('birthdays.csv')
birthdays_dict = birthdays.to_dict(orient="records")

# ------------------------------ CHECK IF IT IS SOMEONE'S BIRTHDAY ------------------------------ #
def birthday_check():
    for entry in birthdays_dict:
        name = entry['name']
        month = entry['month']
        day = entry['day']
        birthday = dt.date(today.year, month=month, day=day)
        if birthday == today:
            print(f"HORRAY!! {name}'s birthday is on the: {birthday}")
            return birthday


# ------------------------------ PREP BIRTHDAY MESSAGE ------------------------------ #



# ------------------------------ SEND BIRTHDAY EMAIL ------------------------------ #


birthday_check()