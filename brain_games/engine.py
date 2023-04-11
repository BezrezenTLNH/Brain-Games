import prompt


def start_games(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print(game.RULE)

    CORRECT_ANSWERS = 0

    while CORRECT_ANSWERS < 3:
        right_answer, question = game.get_question_and_right_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == right_answer:
            print("Correct!")
            CORRECT_ANSWERS += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
