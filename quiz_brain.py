import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_q(self):
        return self.question_number <= len(self.question_list)


    def next_q(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        q_text=html.unescape(current_q.text)
        user_a=input(f" Q.{self.question_number} : {q_text} (True/False)")
        self.check_a(user_a, current_q.answer, )

    def check_a(self, user_a, correct_a,):
        if user_a.lower() == correct_a.lower():
            self.score += 1
            print("You got it right.")
        else:
            print(f"Wrong answer. ")
        print(f" Correct answer was {correct_a}")
        print(f" Your score is {self.score}/{self.question_number}")
        print("\n")