"""Main game logic and output"""

import prompt

ROUND_COUNTS = 3


def play(game):
    print('Welcome to the Brain Games!')
    print(f'{game.GAME_DESCRIPTION}\n')

    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n')

    try_count = ROUND_COUNTS

    while try_count:
        question, correct_answer = game.get_quiz()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            try_count -= 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
