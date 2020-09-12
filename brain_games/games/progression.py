from random import randrange

GAME_DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10
MAX_START = 10
MAX_STEP = 10


def get_quiz():
    start = randrange(1, MAX_START)
    step = randrange(1, MAX_STEP)
    progression = []

    for item in range(start, start + PROGRESSION_LENGTH * step, step):
        progression.append(str(item))

    answer_index = randrange(PROGRESSION_LENGTH)
    answer = progression[answer_index]
    progression[answer_index] = '...'

    question = ' '.join(progression)

    return question, answer
