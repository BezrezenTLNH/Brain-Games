import random
from random import randint
import operator

RULE = 'What is the result of the expression?'


def get_right_answer(first_number, second_number, operation_number):
    if operation_number == '+':
        right_answer = operator.add(first_number, second_number)
    elif operation_number == '-':
        right_answer = operator.sub(first_number, second_number)
    else:
        right_answer = operator.mul(first_number, second_number)
    return right_answer


def get_question_and_right_answer():
    operation_number = random.choice('+-*')
    first_number = randint(1, 25)
    second_number = randint(1, 25)
    question = (
        f'{first_number} {operation_number} {second_number}'
    )

    right_answer = get_right_answer(
        first_number, second_number, operation_number
    )

    return str(right_answer), question
