#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What is the result of the expression?')
    correct_answers = 0
    while correct_answers < 3:
        operation_number = randint(1, 3)
        first_random_number = randint(1, 25)
        second_random_number = randint(1, 25)
        summ = first_random_number + second_random_number
        multiplication = first_random_number * second_random_number
        subtraction = first_random_number - second_random_number

        if operation_number == 1:
            right_answer = summ
            print(f'Question: {first_random_number} '
                  f'+ {second_random_number}')
        elif operation_number == 2:
            right_answer = multiplication
            print(f'Question: {first_random_number} '
                  f'* {second_random_number}')
        else:
            right_answer = subtraction
            print(f'Question: {first_random_number} '
                  f'- {second_random_number}')

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


if __name__ == '__main__':
    main()
