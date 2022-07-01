from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzapp")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Question", width=280, font=("Arial", 16, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_img, highlightthickness=0)
        self.correct_button.grid(row=2, column=0)

        incorrect_img = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(image=incorrect_img, highlightthickness=0)
        self.incorrect_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        next_question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=next_question)
