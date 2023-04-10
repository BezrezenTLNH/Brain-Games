import random
from random import randint

RULE = 'What is the result of the expression?'


def get_question_and_right_answer():
    operation_number = random.choice('+-*')
    first_random_number = randint(1, 25)
    second_random_number = randint(1, 25)
    example = f'{first_random_number} {operation_number} {second_random_number}'
    right_answer = str(eval(example))

    return right_answer, example
