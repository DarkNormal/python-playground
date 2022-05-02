from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    user = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    invalid_input = len(website) == 0 or len(password) == 0
    if invalid_input:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {user}\nPassword: {password}\nOK to save?")

        if is_ok:
            try:
                with open("data.json", "r") as pw_file:
                    data = json.load(pw_file)
            except FileNotFoundError:
                with open("data.json", "w") as pw_file:
                    json.dump(new_data, pw_file, indent=4)
            else:
                with open("data.json", "w") as pw_file:
                    data.update(new_data)
                    json.dump(data, pw_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    try:
        with open("data.json", "r") as pw_file:
            data = json.load(pw_file)
    except FileNotFoundError:
        messagebox.showwarning(title="No passwords", message="No password data file found.")
    else:
        website = website_input.get()
        if website in data:
            messagebox.showinfo(title=f"Details for {website}", message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Not found", message=f"Password details not found for site {website}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width="200", height="200")
canvas.create_image(100, 112, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")

search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=2, sticky="ew")

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.insert(0, "user@example.com")
username_input.grid(row=2, column=1, columnspan=2, sticky="ew")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky="w")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
