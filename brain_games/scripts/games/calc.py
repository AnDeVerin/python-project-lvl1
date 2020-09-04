from random import randrange

GAME_DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = [
    ('*', lambda a, b: a * b),
    ('+', lambda a, b: a + b),
    ('-', lambda a, b: a - b),
]


def get_question():
    a = randrange(10)
    b = randrange(10)
    index = randrange(3)
    operation, calculate = OPERATIONS[index]

    question = f'Question: {a} {operation} {b}'
    answer = str(calculate(a, b))

    return question, answer
