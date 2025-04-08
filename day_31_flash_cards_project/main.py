from tkinter import *
import pandas as pd
from random import *
import os

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Arial', 30, 'italic')
WORD_FONT = ('Arial', 45, 'bold')
PROGRESS_FONT = ('Georgia', 15, 'italic')
LANG_A = 'French'
LANG_B = 'English'
current_language = LANG_A
language_couple = {}
words_to_learn = []
PROGRESS_FILE = 'data/words_to_learn.csv'
data = None

# ---------------------------- MANAGE USER PROGRESS ------------------------------- #
def start_game():
    global words_to_learn, data

    if os.path.exists(PROGRESS_FILE):
        data = pd.read_csv(PROGRESS_FILE)
    else:
        data = pd.read_csv('data/french_words.csv')
        # data = pd.read_csv('data/3_french_words.csv')
    words_to_learn = data.to_dict(orient='records')

def save_progress():
    global words_to_learn, data
    words_to_learn.remove(language_couple)
    canvas2.itemconfig(progress_text, text=f"{len(words_to_learn)} more words to learn")
    data_to_save = pd.DataFrame(words_to_learn)
    data_to_save.to_csv('data/words_to_learn.csv')
    if len(words_to_learn) == 0:
        canvas2.itemconfig(progress_text, text=f"Congrats, you learned all {len(data)} entries!!!")
        os.remove(PROGRESS_FILE)

def end_game():
    exit()

# ---------------------------- DISPLAY WORDS ------------------------------- #
def pick_a_word():
    global language_couple, flip_timer, words_to_learn
    window.after_cancel(flip_timer)
    language_couple = choice(words_to_learn)
    current_word = language_couple[LANG_A]
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(lang_text, text=LANG_A, fill='black')
    canvas.itemconfig(word_lang_text, text=current_word, fill='black')
    flip_timer = window.after(3000, flip_card)

#---------------------------- FLIP THE CARDS ------------------------------- #
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
canvas.grid(row=1,column=0,columnspan=2)

# Progress
canvas2 = Canvas(background=BACKGROUND_COLOR, width=400, height=30, highlightthickness=0)
progress_text = canvas2.create_text(220, 10, text='', fill='black', font=PROGRESS_FONT)
canvas2.grid(row=0,column=1, columnspan=2)


# Buttons
right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')
yes_button = Button(
    image=right_image,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    command= lambda:[save_progress(), pick_a_word()]
    )
yes_button.grid(row=1,column=1)

no_button = Button(
    image=wrong_image,
    highlightthickness=0,
    highlightbackground=BACKGROUND_COLOR,
    command=pick_a_word
)
no_button.grid(row=1,column=0)

exit_button = Button(
    text='End Game',
    font=PROGRESS_FONT,
    fg='black',
    # bg='black',
    highlightthickness=0,
command=end_game)
exit_button.grid(row=1,column=2)


start_game()
pick_a_word()


window.mainloop()
