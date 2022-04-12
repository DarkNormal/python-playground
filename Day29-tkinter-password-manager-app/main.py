from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    user = username_input.get()
    password = password_input.get()

    with open("data.txt", "a") as pw_file:
        pw_file.write(f"{website} | {user} | {password}\n")

    website_input.delete(0, END)
    password_input.delete(0, END)


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

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.insert(0, "user@example.com")
username_input.grid(row=2, column=1, columnspan=2, sticky="ew")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky="w")

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
