from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)

quiz = QuizzBrain(question_bank)
while quiz.still_has_questions():
    score, total = quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {score}/{total}")
