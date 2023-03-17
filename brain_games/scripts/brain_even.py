import prompt
from random import randint


def even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_number = randint(1, 100)
    correct_answers = 0
    if correct_answers <= 3:
        print(f'Question: {random_number}')

        answer = prompt.string('Your answer: ')



