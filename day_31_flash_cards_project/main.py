from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Arial', 30, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
LANG_A = 'French'
LANG_B = 'English'

# ---------------------------- DISPLAY WORDS ------------------------------- #

data = pd.read_csv('data/french_words.csv')

def pick_a_word(lang=LANG_A):
    coupled_words = data.to_dict(orient='records')
    language_couple= choice(coupled_words)
    for lang,word in language_couple.items():
        if lang == LANG_A:
            canvas.itemconfig(lang_text, text=lang, fill='black')
            canvas.itemconfig(word_lang_text, text=word, fill='black')
        # else:
        #     print('been here!')
        #     canvas.itemconfig(lang_text, text=lang, fill='white')
        #     canvas.itemconfig(word_lang_text, text=word, fill='white')



#---------------------------- FLIP THE CARDS ------------------------------- #

def flip_card():
    canvas.after(3000, display_lang_b)
#
def display_lang_b():
    canvas.itemconfig(canvas_image, image=back_image)


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

pick_a_word(LANG_A)
flip_card()

window.mainloop()
