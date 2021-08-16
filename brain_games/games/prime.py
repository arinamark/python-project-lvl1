#!env python
from random import randint


PRIMITIVE = [1, 2]
GEN_PRIME = 100


def is_prime(num):
    if num in PRIMITIVE:
        return 'yes'
    dev = 2
    while dev < num:
        if num % dev == 0:
            return 'no'
        dev += 1
    return 'yes'


def gen_expression():
    a = randint(1, GEN_PRIME)
    result = is_prime(a)
    return (result, str(a))
