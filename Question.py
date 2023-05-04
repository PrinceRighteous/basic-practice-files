class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

q1 = Question("who are you?", "kareem")
print(q1.answer)
# This class works with the Quiz.py file/module this file should be imoorted to the quiz.py file in order to do the multiple choice quiz