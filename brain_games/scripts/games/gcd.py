from random import randrange

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'

MIN_GCD = 2


def get_gcd(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    return get_gcd(b, a % b)


def get_question():
    a = b = gcd = 1

    while gcd < MIN_GCD:
        a = randrange(2, 101)
        b = randrange(2, 101)
        gcd = get_gcd(a, b) if a > b else get_gcd(b, a)

    question = f'{a} {b}'
    answer = str(gcd)

    return question, answer
