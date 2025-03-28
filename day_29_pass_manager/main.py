from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1,row=0)

# Labels
website_l = Label(text='Website:')
website_l.grid(column=0, row=1, padx=5, pady=5)
email_username_l = Label(text='Email/Username:')
email_username_l.grid(column=0, row=2, padx=5, pady=5)
password = Label(text='Password:')
password.grid(column=0, row=3, padx=5, pady=5)

# Entry
website_input = Entry(width=37)
website_input.grid(column=1, row=1, columnspan=2)
username_input = Entry(width=37)
username_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21, justify='left')
password_input.grid(column=1, row=3)


# Buttons
password_gen = Button(text='Generate Password', width=12)
password_gen.grid(column=2, row=3)
add_details = Button(text='Add', width=35)
add_details.grid(column=1, row=4, columnspan=2)

window.mainloop()