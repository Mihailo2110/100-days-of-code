from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
value = 0
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="adsfgh", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.label = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}", bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0, padx=20, pady=20)
        self.cross_image = PhotoImage(file="images/false.png")
        self.unknown_button = Button(image=self.cross_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.unknown_button.grid(column=1, row=2, padx=20, pady=20)
        self.check_image = PhotoImage(file="images/true.png")
        self.known_button = Button(image=self.check_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.known_button.grid(column=0, row=2, padx=20, pady=20)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.known_button.config(state="disabled")
            self.unknown_button.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



