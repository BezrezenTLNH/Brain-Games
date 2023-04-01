#!/usr/bin/env python3
import prompt
from brain_games import games


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What is the result of the expression?')

    games.game_calc(user_name)


if __name__ == '__main__':
    main()
