from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count, time_text):
    if count >= 0:
        canvas.itemconfig(time_text, text=count)
        canvas.after(1000, count_down, count - 1, time_text)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(99, 112, image=tomato_img)
timer_text = canvas.create_text(99,130, text='00:00', fill='white', font=(FONT_NAME, 31, 'bold'))
canvas.grid(column=1, row=1)
count_down(5, timer_text)

# Buttons
start_button = Button(text='Start', width=3, bg=YELLOW, border=0, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset', width=3, bg=YELLOW, border=0, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Check-marks
check_mark = Label(text='✓', font=(FONT_NAME,35), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)
# Timer label
timer_l = Label(text='Timer', font=(FONT_NAME, 45), bg=YELLOW, fg=GREEN)
timer_l.grid(column=1, row=0)


window.mainloop()