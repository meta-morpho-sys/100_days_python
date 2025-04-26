from tkinter import *


THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 12, "bold")

class QuizzInterface():
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=35, padx=35)
        self.canvas = Canvas(width=400, height=250, bg='white')
        self.question_text = self.canvas.create_text(200, 125, text="hello there", font=QUESTION_FONT)
        self.canvas.grid(row=1, columnspan=2, pady=50)
        # Buttons
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(
            image=true_image,
            padx=20,
            pady=20,
            highlightbackground=THEME_COLOR
        ).grid(row=2,column=1)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(
            image=false_image,
            padx=20,
            pady=20,
            highlightbackground=THEME_COLOR
        ).grid(row=2, column=0)
        # Score
        self.score = Label(text='Score: 0', font=SCORE_FONT, bg=THEME_COLOR, fg='white', padx=20,pady=20,).grid(row=0, column=1)

        self.window.mainloop()

