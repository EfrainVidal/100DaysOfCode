from tkinter import *
import math

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

def reset_time():
    # stop the timer
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_time "Timer"
    title_label.config(text="Timer")
    # reset check_marks
    check_label.config(text="")
    # reset the reps
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    # call the countdown function to update text
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # if it's the 8th rep:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # if it's the 2nd/4th/6th rep:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        # if it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    # get number of minutes to display
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = F"0{count_sec}"

    # in order to change canvas text, call the canvas.itemconfig()
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # after means to delay and then do something after that amount of time
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # add a check mark each time the timer completes a work session
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# image in background
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # set the size and color of the canvas
tomato_img = PhotoImage(file="tomato.png") # get a hold of the image file and save it to a variable
canvas.create_image(100, 112, image=tomato_img) # add the image variable file to the canvas
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 28,  "bold"))
canvas.grid(column=1, row=1) # add the image to the screen

#timer label
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "normal"))
title_label.grid(column=1, row=0)

# Buttons start and reset
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_time)
reset_btn.grid(column=2, row=2)

# check label
check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)




window.mainloop()
