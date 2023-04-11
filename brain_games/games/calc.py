import random
from random import randint

RULE = 'What is the result of the expression?'


def get_question_and_right_answer():
    operation_number = random.choice('+-*')
    first_random_number = randint(1, 25)
    second_random_number = randint(1, 25)
    question = f'{first_random_number} ' \
               f'{operation_number} {second_random_number}'
    if operation_number == '+':
        right_answer = first_random_number.__add__(second_random_number)
    elif operation_number == '-':
        right_answer = first_random_number.__sub__(second_random_number)
    else:
        right_answer = first_random_number.__mul__(second_random_number)
    right_answer = str(right_answer)

    return right_answer, question
