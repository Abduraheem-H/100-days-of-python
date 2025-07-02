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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    min = (count) // 60
    sec = (count) % 60
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        global reps
        start_timer()
        marks = "✔" * (reps // 2)
        checkmarks_label.config(text=marks)
    canvas.itemconfig(timer_text, text=f"{min:02d}:{sec:02d}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(
    text="Timer",
    fg=GREEN,
    font=(FONT_NAME, 50),
    bg=YELLOW,
)
timer_label.grid(row=0, column=1)

checkmarks_label = Label(text="", fg=GREEN, bg=YELLOW)
checkmarks_label.grid(row=3, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)
reset_btn = Button(text="Reset", highlightthickness=0, command=reset_time)
reset_btn.grid(row=2, column=2)


window.mainloop()
