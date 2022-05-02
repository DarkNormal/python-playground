from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
random_word = {}
translation_data = []


# --------------- DATA CSV LOAD ----------#

def load_data():
    global translation_data
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        original_data = pandas.read_csv("data/french_words.csv")
        translation_data = original_data.to_dict(orient="records")
    else:
        translation_data = data.to_dict(orient="records")


# --------------- CLICK METHODS ----------#

def show_solution_card():
    global random_word
    # To change the image:
    canvas.itemconfig(canvas_img, image=solution_card_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")


def next_card():
    global random_word, flip_timer

    window.after_cancel(flip_timer)
    random_word = random.choice(translation_data)
    print(random_word)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_img)

    flip_timer = window.after(3000, func=show_solution_card)


def correct_word():
    translation_data.remove(random_word)
    print(translation_data)
    print(len(translation_data))
    data = pandas.DataFrame(translation_data)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# --------------- UI SETUP ---------------#

load_data()

window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

solution_card_img = PhotoImage(file="images/card_back.png")
card_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(width="800", height="550", bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 275, image=card_img)
canvas.grid(row=0, column=0, columnspan=2)

# text in card
language = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))

# buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=correct_word)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, func=show_solution_card)

next_card()

window.mainloop()
