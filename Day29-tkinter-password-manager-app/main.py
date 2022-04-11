from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width="200", height="200")
canvas.create_image(100, 112, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky="ew")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=32)
password_input.grid(row=3, column=1, sticky="w")

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
