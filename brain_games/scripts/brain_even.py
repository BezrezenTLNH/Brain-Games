#!/usr/bin/env python3
from brain_games.engine import start_games
from brain_games.games import even


def main():
    start_games(even)


if __name__ == '__main__':
    main()
