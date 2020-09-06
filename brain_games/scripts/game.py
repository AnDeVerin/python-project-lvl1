"""Main game logic and output"""

import prompt

COUNT = 3


def check_quiz(get_question, count):
    try_count = count

    while try_count:
        question, correct_answer = get_question()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            try_count -= 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            return False

    return True


def start_game(game=None):
    if game is None:
        print('Exit: no game was passed.')
        return

    print('Welcome to the Brain Games!')
    print(f'{game.GAME_DESCRIPTION}\n')

    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n')

    is_winner = check_quiz(game.get_question, COUNT)

    if is_winner:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")
