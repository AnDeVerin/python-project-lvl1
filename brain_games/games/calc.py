from random import randrange
import operator

GAME_DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = [
    ('*', operator.mul),
    ('+', operator.add),
    ('-', operator.sub),
]


def get_quiz():
    a = randrange(10)
    b = randrange(10)
    index = randrange(len(OPERATIONS))
    operation, calculate = OPERATIONS[index]

    question = f'{a} {operation} {b}'
    answer = str(calculate(a, b))

    return question, answer
