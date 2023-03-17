#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
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


if __name__ == '__main__':
    main()
