"""Main game logic and output"""

import prompt

# https://ru.hexlet.io/courses/python-lists/lessons/for-loop/theory_unit
ROUNDS = 3


def play(game):
    print('Welcome to the Brain Games!')
    print(f'{game.GAME_DESCRIPTION}\n')

    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n')

    tries = ROUNDS

    while tries:
        question, correct_answer = game.get_quiz()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            tries -= 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
