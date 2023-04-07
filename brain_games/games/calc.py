from random import randint

RULE = 'What is the result of the expression?'


def brain_play():
    operation_number = randint(1, 3)
    first_random_number = randint(1, 25)
    second_random_number = randint(1, 25)

    if operation_number == 1:
        summ = first_random_number + second_random_number
        right_answer = summ
        example = f'{first_random_number} + {second_random_number}'
    elif operation_number == 2:
        multiplication = first_random_number * second_random_number
        right_answer = multiplication
        example = f'{first_random_number} * {second_random_number}'
    else:
        if first_random_number >= second_random_number:
            biggest_number = first_random_number
            smallest_number = second_random_number
        else:
            biggest_number = second_random_number
            smallest_number = first_random_number
        example = f'{biggest_number} - {smallest_number}'
        subtraction = biggest_number - smallest_number
        right_answer = subtraction
    right_answer = str(right_answer)

    return right_answer, example
