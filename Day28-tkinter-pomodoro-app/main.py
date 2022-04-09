from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK_TEXT = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    global timer

    reps = 0
    window.after_cancel(timer)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        countdown_timer(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        countdown_timer(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        countdown_timer(short_break_sec)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown_timer(count):
    global timer
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(500, countdown_timer, count - 1)
    else:
        start_timer()
        checkmark_label.config(text=CHECKMARK_TEXT * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width="200", height="224", bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset)
reset_btn.grid(row=2, column=2)

checkmark_label = Label(text="", fg=GREEN)
checkmark_label.grid(row=3, column=1)

window.mainloop()
