from random import randrange

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'

min_gcd = 2


def get_gcd(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    if a > b:
        return get_gcd(b, a % b)

    else:
        return get_gcd(a, b % a)


def get_question():
    gcd = 0

    while gcd < min_gcd:
        a = randrange(2, 101)
        b = randrange(2, 101)
        gcd = get_gcd(a, b)

    question = f'Question: {a} {b}'
    answer = str(gcd)

    return question, answer
