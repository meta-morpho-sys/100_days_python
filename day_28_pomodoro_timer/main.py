import math
from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    canvas.after_cancel(timer)
    title_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # 4-Pomodoro Cycle + Long break
    if reps % 2 == 0 and not reps % 8 == 0:
        # If it is the 2nd, 4th, 6th repetition
        print("SHORT BREAK")
        title_label.config(text="Take a short break", fg=PINK)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        print("LONG BREAK")
        title_label.config(text="Take a long break", fg=GREEN)
        count_down(long_break_sec)
    else:
        # If it is the 1st, 3rd, 5th, 7th repetition
        print("WORK")
        title_label.config(text="Start concentrating", fg=RED)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(seconds):
    count_min = floor(seconds / 60)
    count_sec = seconds % 60
    if count_sec == 0:
        count_sec = "00"
    if int(count_sec) < 10 and not int(count_sec) == 0:
        count_sec = f"0{count_sec}"
    if  count_min <= 9 or count_min ==0:
        count_min = f"0{count_min}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if seconds > 0:
        global timer
        timer = canvas.after(1000, count_down, seconds - 1)
    else:
        start_count()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in  range(work_sessions):
            marks += '✓'
            check_mark.config(text=f"Pomodoros completed: {marks}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(99, 112, image=tomato_img)
timer_text = canvas.create_text(99, 130, text=f"{WORK_MIN}:00", fill='white', font=(FONT_NAME, 31, 'bold'))
canvas.grid(column=1, row=1)


# Buttons
start_button = Button(text='Start', width=3, bg=YELLOW, border=0, highlightthickness=0, command=start_count)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset', width=3, bg=YELLOW, border=0, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check-marks
check_mark = Label(text='', font=(FONT_NAME, 25), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

# Timer label
title_label = Label(text='Timer', font=(FONT_NAME, 45), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)


window.mainloop()