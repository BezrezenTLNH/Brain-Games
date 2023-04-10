from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    example = randint(1, 100)

    if (example % 2) == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, example
