from random import randrange
from brain_games.scripts.cli_utils import get_string_from_user


def play_even_game():
    try_count = 3

    while try_count:
        number = randrange(100)
        correct_answer = 'yes' if (number % 2 == 0) else 'no'

        print(f'Question: {number}')
        user_answer = get_string_from_user('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            try_count -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            return False

    return True
