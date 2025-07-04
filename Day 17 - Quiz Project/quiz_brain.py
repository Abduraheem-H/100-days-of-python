class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number} {curr_question.text} (True/False)?: "
        ).title()
        self.check_answer(user_answer, curr_question.answer)
        return (self.score, self.question_number)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it!")
        else:
            print("You got it wrong!")

        print(f"The correct answer was {user_answer}")
        print(f"Your current score {self.score}/{self.question_number}")
        print("\n")
