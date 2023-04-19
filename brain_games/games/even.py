from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return right_answer


def get_question_and_right_answer():
    question = randint(1, 100)
    right_answer = is_even(question)
    return right_answer, question
