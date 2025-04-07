from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Arial', 30, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
LANG_A = 'French'
LANG_B = 'English'
current_language = LANG_A
flip = None

data = pd.read_csv('data/french_words.csv')
language_data = data.to_dict(orient='records')
language_couple = {}
# ---------------------------- DISPLAY WORDS ------------------------------- #

def pick_a_word():
    global language_couple, flip_timer
    window.after_cancel(flip_timer)
    language_couple = choice(language_data)
    word = language_couple[LANG_A]
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(lang_text, text=LANG_A, fill='black')
    canvas.itemconfig(word_lang_text, text=word, fill='black')
    flip_timer = window.after(3000, flip_card)

#---------------------------- FLIP THE CARDS ------------------------------- #

#
def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    word = language_couple[LANG_B]
    canvas.itemconfig(lang_text, text=LANG_B, fill='white')
    canvas.itemconfig(word_lang_text, text=word, fill='white')



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(f"Learn {LANG_A} With Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

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



window.mainloop()
