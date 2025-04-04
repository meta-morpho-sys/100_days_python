import random
from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Arial', 30, 'italic')
WORD_FONT = ('Arial', 60, 'bold')

# ---------------------------- MECHANISM TO DISPLAY WORDS ------------------------------- #

data = pd.read_csv('data/french_words.csv')

def pick_a_word():
    coupled_words = data.to_dict(orient='records')
    print(coupled_words[randint(0, len(coupled_words))])

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(background=BACKGROUND_COLOR, width=900, height=600, highlightthickness=0)
front_image = PhotoImage(file='images/card_front.png')
canvas.create_image(460,300, image=front_image)
canvas.create_text(460, 300, text='Word',font=WORD_FONT)
canvas.create_text(460, 150, text='Language',font=LANGUAGE_FONT)
canvas.grid(row=0,column=0,columnspan=2)


# Buttons
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')
yes_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=pick_a_word)
yes_button.grid(row=1,column=1)

no_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=pick_a_word)
no_button.grid(row=1,column=0)



window.mainloop()
