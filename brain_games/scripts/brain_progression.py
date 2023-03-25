#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What number is missing in the progression?')
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


if __name__ == '__main__':
    main()
