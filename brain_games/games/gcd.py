from random import randint
import math

RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_right_answer():
    multiplication_number = randint(2, 5)
    first_random_number = randint(1, 25) * multiplication_number
    second_random_number = randint(1, 25) * multiplication_number
    question = f'{first_random_number} {second_random_number}'
    right_answer = str(math.gcd(first_random_number, second_random_number))

    return right_answer, question
