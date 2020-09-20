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
    operator_symbol, operation = OPERATIONS[index]

    question = f'{a} {operator_symbol} {b}'
    answer = str(operation(a, b))

    return question, answer
