
#  It's supporting file is question.py

from question import Question

question_promts = [
    "What colour are Apples? \n(a) Red/Green\n(b) Purple\n(c) Orange\n\n ",
    "What colour are Bananas? \n(a) Teal\n(b) Magenta\n(c) Yellow\n\n ",
    "What colour are Strawberries? \n(a) Yellow\n(b) Red\n(c) Blue\n\n ",
]


questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "c"),
    Question(question_promts[2], "b")
]


def run_test(jpt):
    score = 0
    for Question in questions:  #  For each qus in obj Question, I want to do sth
        answer = input(Question.prompt)
        if answer == Question.ans:
            score += 1
    print("You got "+ str(score) +" / " + str(len(questions)) + " Correct !")


run_test(questions)

