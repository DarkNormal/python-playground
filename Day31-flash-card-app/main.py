from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# --------------- DATA CSV LOAD ----------#

data = pandas.read_csv("data/french_words.csv")
translation_dict = data.to_dict(orient="records")


# --------------- CLICK METHODS ----------#

def click():
    random_word = random.choice(translation_dict)
    print(random_word)
    canvas.itemconfig(word, text=random_word["French"])


# --------------- UI SETUP ---------------#

window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width="800", height="550", bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 275, image=card_img)
canvas.grid(row=0, column=0, columnspan=2)

# text in card
language = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))

# buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=click)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=click)
right_button.grid(row=1, column=1)

window.mainloop()
