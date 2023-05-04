# we built a multiple choice quiz this quiz only works with the question class we created in the question.py file/module you must import that class in order for this to work
from Question import Question
question_prompts = [ "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n".title(),
                     "what color are Bananas?\n(a) Teal\n(b) Magneta\n(c) Yellow\n\n".title(),
                     "What color are Strawberries?\n(a) yellow\n(b) red\n(c) Blue\n\n".title()
                     ]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("your final score is " + str(score) + "/" + str(len(questions)))
    if score == 0:
            return "your trash you got none right."
    elif score == 1:
        return "Really just one your still trash. "
    elif score == 2:
        return "brother or sister you can do better."
    else:
        return "great job your really gonna be someone one day!"




print(run_test(questions))

