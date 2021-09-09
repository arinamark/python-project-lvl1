#!env python
from random import randint


PRIMITIVE = [1, 2]
MAX_INT_FOR_RANDOM = 100
rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def gen_game_step():
    a = randint(1, MAX_INT_FOR_RANDOM)
    if is_prime(a):
        answer = 'yes'
    else:
        answer = 'no'
    return answer, str(a)


def is_prime(num):
    if num in PRIMITIVE:
        return True
    dev = 2
    while dev < num:
        if num % dev == 0:
            return False
        dev += 1
    return True
