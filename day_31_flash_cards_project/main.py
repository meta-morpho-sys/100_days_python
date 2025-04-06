from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Arial', 30, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
LANG_A = 'French'
LANG_B = 'English'
flip = None

# ---------------------------- DISPLAY WORDS ------------------------------- #

data = pd.read_csv('data/french_words.csv')

def pick_a_word(language=LANG_A):
    language_data = data.to_dict(orient='records')
    language_couple= choice(language_data)
    if language == LANG_A:
        word = language_couple[LANG_A]
        canvas.itemconfig(lang_text, text=LANG_A, fill='black')
        canvas.itemconfig(word_lang_text, text=word, fill='black')
    else:
        word = language_couple[LANG_B]
        canvas.itemconfig(lang_text, text=LANG_B, fill='white')
        canvas.itemconfig(word_lang_text, text=word, fill='white')



#---------------------------- FLIP THE CARDS ------------------------------- #

def flip_card():
    global flip
    flip = window.after(3000, display_back)

#
def display_back():
    canvas.itemconfig(canvas_image, image=back_image)
    pick_a_word(LANG_B)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(background=BACKGROUND_COLOR, width=900, height=600, highlightthickness=0)
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(460,300, image=front_image)
lang_text = canvas.create_text(460, 150, text='', fill='black', font=LANGUAGE_FONT)
word_lang_text = canvas.create_text(460, 300, text='', fill='black', font=WORD_FONT)
canvas.grid(row=0,column=0,columnspan=2)


# Buttons
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')
yes_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=pick_a_word)
yes_button.grid(row=1,column=1)

no_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=pick_a_word)
no_button.grid(row=1,column=0)

pick_a_word()
flip_card()

window.mainloop()
