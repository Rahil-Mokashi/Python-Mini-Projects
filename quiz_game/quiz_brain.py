class QuizBrain:

    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank
        self.score = 0 

    def still_any_questions(self):
        length = len(self.question_list)
        return self.question_no < length


    def next_question(self):
        current_ques = self.question_list[self.question_no]

        self.question_no += 1

        user_answer = input(f"Q.{self.question_no}. {current_ques.text} (True/False): ").lower()

        self.check_answer(user_answer, current_ques.answer)

    def check_answer(self, user_answer, correct_ans):
        if user_answer.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Oops, you were wrong!")
        print(f"The correct answer: {correct_ans}")
        print(f"Your current score: {self.score}/{self.question_no}")

        

    def final_score(self):
        print("You have completed the Quiz!")
        print(f"Your final score: {self.score}/{self.question_no}")



        


        

