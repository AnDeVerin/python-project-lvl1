from random import randrange

GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def get_question():
    number = randrange(100)
    question = str(number)
    answer = 'yes' if (number % 2 == 0) else 'no'

    return question, answer
