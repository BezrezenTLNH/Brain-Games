#!/usr/bin/env python3
import prompt
from brain_games import games


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    games.game_even(user_name)


if __name__ == '__main__':
    main()
