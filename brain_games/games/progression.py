from random import randint

RULE = 'What number is missing in the progression?'


def get_progression(progression_length, progression, progression_step):
    i = 1
    while i < progression_length:
        next_progression_number = progression[i - 1] + progression_step
        progression.append(next_progression_number)
        i += 1
    return progression


def get_question_and_right_answer():
    progression_length = randint(5, 10)
    progression = [randint(1, 25)]
    progression_step = randint(2, 10)
    question_number_position = randint(0, (progression_length - 1))
    current_progression = get_progression(
        progression_length, progression, progression_step
    )
    right_answer = current_progression[question_number_position]
    current_progression[question_number_position] = '..'
    question = " ".join(map(str, current_progression))
    return str(right_answer), question
