from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1,row=1)

# Labels
website_l = Label()

email_username_l = Label()

password = Label()

# Entry
website_input = Entry()
username_input = Entry()
password_input = Entry()


# Buttons
password_gen = Button()
add_details = Button()

window.mainloop()