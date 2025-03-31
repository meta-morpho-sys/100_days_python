from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json

LOGO_RED='#D84040'
FONT=('Arial', 10, 'bold')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def provide_password_string():
    psswd = generate_password()
    password_input.insert(0, psswd)
    pyperclip.copy(psswd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Take values for all 3 inputs and store them in a file
    # TODO: Password needs encryption
    website = website_input.get().lower()
    username = username_input.get()
    pswd = password_input.get()
    new_data = {
        website: {
            'email': username,
            'password': pswd
        }
    }

    # Validation
    entries = [website,username,pswd]
    empty_fields = [messagebox.showerror(
        title='Empty Fields Warning',
        message="Please, don't leave any fields empty") for entry in entries if "".__eq__(entry)]
    if not empty_fields:
        try:
            data = update_data_entry(new_data)
        except FileNotFoundError:
            create_data_entry(new_data)
            messagebox.showinfo(message="Username and Password saved")
        else:
            create_data_entry(data)
            messagebox.showinfo(message="Username and Password saved")
        finally:
            website_input.delete(0, END)
            password_input.delete(0,END)


def create_data_entry(data):
    with open('data.json', 'w') as data_file:
        # Write new data
        json.dump(data, data_file, indent=4)


def update_data_entry(new_data):
    with open('data.json', 'r') as data_file:
        # Read old data
        data = json.load(data_file)
        # Update old data with new data
        data.update(new_data)
    return data

# ---------------------------- FIND PASSWORD ------------------------------- #

def search_password():
    website = website_input.get().lower()
    try:
        with open('data.json', 'r') as search_data_file:
            search_data = json.load(search_data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Usernames and Passwords found.\nIs this the first time you are using your Password Manager?")
    else:
        if website in search_data:
            username = search_data[website]['email']
            pswd = search_data[website]['password']
            messagebox.showinfo(message=f"Username is: {username}\nPassword is: {pswd}")
        else:
            messagebox.showinfo(f"No details for {website} website in your Password Manager.You can create it now")
    finally:
        website_input.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1,row=0)

# Labels
website_l = Label(text='Website:', font=FONT, fg=LOGO_RED)
website_l.grid(column=0, row=1, padx=5, pady=5)
email_username_l = Label(text='Email/Username:', font=FONT, fg=LOGO_RED)
email_username_l.grid(column=0, row=2, padx=5, pady=5)
password = Label(text='Password:', font=FONT, fg=LOGO_RED)
password.grid(column=0, row=3, padx=5, pady=5)

# Entry
website_input = Entry(width=22)
website_input.focus()
website_input.grid(column=1, row=1)
username_input = Entry(width=37)
username_input.insert(0, 'yuliya@banana.com')
username_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=22, justify='left')
password_input.grid(column=1, row=3)


# Buttons
password_gen = Button(text='Generate Password', fg=LOGO_RED, font=FONT, width=12, command=provide_password_string)
password_gen.grid(column=2, row=3)
add_details = Button(text='Add', fg=LOGO_RED, font=FONT, width=35, command=save)
add_details.grid(column=1, row=4, columnspan=2)
search_details = Button(text='Search', fg=LOGO_RED, font=FONT, width=12, command=search_password)
search_details.grid(column=2, row=1)

window.mainloop()