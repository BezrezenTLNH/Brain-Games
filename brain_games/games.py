#!/usr/bin/env python3
import prompt
from random import randint


def game_prime(user_name):
    correct_answers = 0

    while correct_answers < 3:

        current_number = randint(1, 2)
        i = 1
        divider = 0

        while i <= current_number:
            if (current_number % i) == 0:
                divider += 1
                i += 1
            else:
                i += 1

        if (divider <= 2) and (current_number != 1):
            right_answer = 'yes'
        else:
            right_answer = 'no'

        print(f'Question: {current_number}')

        user_answer = prompt.string('Your answer: ')
        user_answer = user_answer.lower()

        if user_answer == right_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break

    if correct_answers == 3:
        print(f'Congratulations, {user_name}!')


def game_calc(user_name):
    correct_answers = 0

    while correct_answers < 3:
        operation_number = randint(1, 3)
        first_random_number = randint(1, 25)
        second_random_number = randint(1, 25)

        if operation_number == 1:
            summ = first_random_number + second_random_number
            right_answer = summ
            print(f'Question: {first_random_number} '
                  f'+ {second_random_number}')
        elif operation_number == 2:
            multiplication = first_random_number * second_random_number
            right_answer = multiplication
            print(f'Question: {first_random_number} '
                  f'* {second_random_number}')
        else:
            if first_random_number >= second_random_number:
                biggest_number = first_random_number
                smallest_number = second_random_number
            else:
                biggest_number = second_random_number
                smallest_number = first_random_number
            subtraction = biggest_number - smallest_number
            right_answer = subtraction
            print(f'Question: {biggest_number} '
                  f'- {smallest_number}')

        user_answer = prompt.integer('Your answer: ')

        if user_answer == right_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break

        if correct_answers == 3:
            print(f'Congratulations, {user_name}!')


def game_even(user_name):
    correct_answers = 0
    while correct_answers < 3:
        current_random_number = randint(1, 100)
        if (current_random_number % 2) == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print(f'Question: {current_random_number}')

        user_answer = prompt.string('Your answer: ')
        user_answer = user_answer.lower()

        if user_answer == right_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break
        if correct_answers == 3:
            print(f'Congratulations, {user_name}!')


def game_gcd(user_name):
    correct_answers = 0

    while correct_answers < 3:
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

        print(f'Question: {first_random_number} {second_random_number}')

        user_answer = prompt.integer('Your answer: ')

        if user_answer == right_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break

        if correct_answers == 3:
            print(f'Congratulations, {user_name}!')


def game_progression(user_name):
    correct_answers = 0

    while correct_answers < 3:
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
        question = " ".join(map(str, progression))

        print(f'Question: {question}')

        user_answer = prompt.integer('Your answer: ')

        if user_answer == right_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break

        if correct_answers == 3:
            print(f'Congratulations, {user_name}!')
