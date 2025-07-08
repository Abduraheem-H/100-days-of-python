from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.timer = None
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Some Text here", font=FONT, fill=THEME_COLOR
        )

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.score_label = Label(text="Score 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.false_btn = Button(
            image=false_img, highlightthickness=0, command=self.get_false_answer
        )
        self.false_btn.grid(row=2, column=1)
        self.true_btn = Button(
            image=true_img, highlightthickness=0, command=self.get_true_answer
        )
        self.true_btn.grid(row=2, column=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.timer:
            self.window.after_cancel(self.timer)
            self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You have reached the end of the Quiz",
                fill=THEME_COLOR,
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def get_true_answer(self):
        self.give_user_feedback(self.quiz.check_answer("True"))

    def get_false_answer(self):
        self.give_user_feedback(self.quiz.check_answer("False"))

    def give_user_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.timer = self.window.after(1000, self.get_next_question)
