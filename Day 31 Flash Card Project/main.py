from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
curent_card = {}
data = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")

finally:
    data_dict = data.to_dict(orient="records")
    if not data_dict:
        messagebox.showinfo(title="Done!", message="You've learned all the words!")


def next_learned_card():
    global curent_card
    data_dict.remove(curent_card)
    pd.DataFrame(data_dict).to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global curent_card, flip_timer
    window.after_cancel(flip_timer)
    curent_card = random.choice(data_dict)

    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_language, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{curent_card['French']}", fill="black")
    flip_timer = window.after(
        3000,
        func=flip_card,
    )


def flip_card():

    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{curent_card['English']}", fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_language = canvas.create_text(
    400, 150, font=("Ariel", 40, "italic"), text="French"
)
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="")
canvas.grid(row=0, column=0, columnspan=2)


unknown_image = PhotoImage(file="./images/wrong.png")
unknown_btn = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

known_image = PhotoImage(file="./images/right.png")
known_btn = Button(image=known_image, highlightthickness=0, command=next_learned_card)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()
