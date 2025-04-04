from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(background=BACKGROUND_COLOR, width=900, height=600, highlightthickness=0)
front_image = PhotoImage(file='images/card_front.png')
canvas.create_image(460,300, image=front_image)
canvas.grid(row=0,column=0,columnspan=2)


# Buttons
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')
yes_button = Button(image=right_image, highlightthickness=0)
yes_button.grid(row=1,column=1)

no_button = Button(image=wrong_image, highlightthickness=0)
no_button.grid(row=1,column=0)
window.mainloop()
