from tkinter import *
from tkinter import messagebox
from password_generator import generate_password

LOGO_RED='#D84040'
FONT=('Arial', 10, 'bold')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def provide_password_string():
    psswd = generate_password()
    password_input.insert(0, psswd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Take values for all 3 inputs and store them in a file
    # TODO: Password needs encryption
    website = website_input.get()
    username = username_input.get()
    pswd = password_input.get()

    # Validation
    entries = [website,username,pswd]
    empty_fields = [messagebox.showerror(
        title='Empty Fields Warning',
        message="Please, don't leave any fields empty") for entry in entries if "".__eq__(entry)]
    if not empty_fields:
        message = f"Are these entries correct?\n\nUsername: {username}\nPassword: {pswd}"
        is_ok = messagebox.askokcancel(title=website, message=message)
        if is_ok:
            new_entry = f"{website},{username},{pswd}\n"
            with open('data.csv', 'a') as data:
                data.write(new_entry)
            website_input.delete(0,END)
            password_input.delete(0,END)
            messagebox.showinfo(message="Username and Password saved")


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
website_input = Entry(width=37)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)
username_input = Entry(width=37)
username_input.insert(0, 'yuliya@banana.com')
username_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=22, justify='left')
password_input.grid(column=1, row=3)


# Buttons
password_gen = Button(text='Generate Password', font=FONT, width=12, command=provide_password_string)
password_gen.grid(column=2, row=3)
add_details = Button(text='Add', font=FONT, width=35, command=save)
add_details.grid(column=1, row=4, columnspan=2)

window.mainloop()