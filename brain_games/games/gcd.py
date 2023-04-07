from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def brain_play():
    multiplication_number = randint(2, 5)
    first_random_number = randint(1, 25) * multiplication_number
    second_random_number = randint(1, 25) * multiplication_number
    i = multiplication_number

    if first_random_number >= second_random_number:
        biggest_number = first_random_number
    else:
        biggest_number = second_random_number

    while i <= biggest_number:

        if (first_random_number % i == 0) \
                and (second_random_number % i == 0):
            right_answer = i
            i += 1
        else:
            i += 1
    example = f'{first_random_number} {second_random_number}'
    right_answer = str(right_answer)

    return right_answer, example
