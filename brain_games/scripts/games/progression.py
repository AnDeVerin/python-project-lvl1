from random import randrange

GAME_DESCRIPTION = 'What number is missing in the progression?'

progression_length = 10
max_start = 10
max_step = 10


def get_question():
    start = randrange(1, max_start)
    step = randrange(1, max_step)
    progression = []

    for item in range(start, start + progression_length * step, step):
        progression.append(str(item))

    answer_index = randrange(progression_length)
    answer = progression[answer_index]
    progression[answer_index] = '...'

    question = ' '.join(progression)

    return question, answer
