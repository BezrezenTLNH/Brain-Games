from random import randint

RULE = 'What number is missing in the progression?'


def get_question_and_right_answer():
    progression_length = randint(5, 10)
    progression = [randint(1, 25)]
    progression_step = randint(2, 10)
    i = 1
    question_number_position = randint(0, (progression_length - 1))

    while i < progression_length:
        next_progression_number = progression[i - 1] + progression_step
        progression.append(next_progression_number)
        i += 1

    right_answer = progression[question_number_position]
    progression[question_number_position] = '..'
    example = " ".join(map(str, progression))
    right_answer = str(right_answer)

    return right_answer, example
