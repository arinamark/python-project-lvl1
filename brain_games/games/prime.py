#!env python
from random import randint


PRIMITIVE = [1, 2]
MAX_INT_FOR_RANDOM = 100
rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def gen_expression():
    a = randint(1, MAX_INT_FOR_RANDOM)
    answer = prime(a)
    return (answer, str(a))


def prime(num):
    if num in PRIMITIVE:
        return 'yes'
    dev = 2
    while dev < num:
        if num % dev == 0:
            return 'no'
        dev += 1
    return 'yes'
