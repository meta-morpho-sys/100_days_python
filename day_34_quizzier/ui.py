from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 12, "bold")

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=35, padx=35)
        self.canvas = Canvas(width=400, height=250, bg='white')
        self.question_text = self.canvas.create_text(200, 125, width=380, text="", font=QUESTION_FONT)
        self.canvas.grid(row=1, columnspan=2, pady=50)

        # BUTTONS
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(
            image=true_image,
            padx=20,
            pady=20,
            highlightbackground=THEME_COLOR,
            command=self.check_positive_answer
        )
        self.true_button.grid(row=2,column=1)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(
            image=false_image,
            padx=20,
            pady=20,
            highlightbackground=THEME_COLOR,
            command=self.check_negative_answer
        )
        self.false_button.grid(row=2, column=0)

        # SCORE
        self.score = Label(text='Score: 0', font=SCORE_FONT, bg=THEME_COLOR, fg='white', padx=20, pady=20,)
        self.score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=question)


    def check_positive_answer(self):
        result = self.quiz_brain.check_answer('True')
        print(result)
        self.get_next_question()

    def check_negative_answer(self):
        result = self.quiz_brain.check_answer('False')
        print(result)
        self.get_next_question()

