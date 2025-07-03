from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_btn():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        random.choices(letters, k=nr_letters)
        + random.choices(symbols, k=nr_symbols)
        + random.choices(numbers, k=nr_numbers)
    )

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def handle_add():
    web_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not web_name or not email or not password:
        messagebox.showerror(
            title="Error", message="Please fill out all fields before saving."
        )
        return

    is_ok = messagebox.askokcancel(
        title=web_name,
        message=f"These are the details entered:\nWebsite: {web_name}\nEmail: {email}\nPassword: {password}\nIs it ok to save?",
    )
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{web_name} | {email} | {password} \n")
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas with logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass_btn = Button(text="Generate Password", command=generate_btn)
generate_pass_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=handle_add)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
