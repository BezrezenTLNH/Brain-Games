from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def brain_play():
    example = randint(1, 25)
    i = 1
    divider = 0

    while i <= example:
        if (example % i) == 0:
            divider += 1
            i += 1
        else:
            i += 1

    if (divider <= 2) and (example != 1):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, example
