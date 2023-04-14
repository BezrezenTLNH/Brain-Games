from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    i = 2
    divider = 0
    while i <= question:
        if (question % i) == 0:
            divider += 1
            i += 1
        else:
            i += 1

    if divider < 2:
        return True
    else:
        return False


def get_question_and_right_answer():
    question = randint(1, 25)

    right_answer = 'yes' if is_prime(question) and question > 1 else 'no'

    return right_answer, question
