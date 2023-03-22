#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Find the greatest common divisor of given numbers.')
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


if __name__ == '__main__':
    main()
