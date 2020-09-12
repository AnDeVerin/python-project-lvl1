from random import randrange
from math import sqrt, ceil

GAME_DESCRIPTION = \
    'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            return False

    return True


def get_quiz():
    number = randrange(100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'

    return question, answer
