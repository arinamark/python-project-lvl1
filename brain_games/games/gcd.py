#!env python
from random import randint
from math import gcd


MAX_INT_FOR_RANDOM = 50
rule = 'Find the greatest common divisor of given numbers.'


def gen_expression():
    a = randint(0, MAX_INT_FOR_RANDOM)
    b = randint(0, MAX_INT_FOR_RANDOM)
    answer = gcd(a, b)
    expression = '{} {}'.format(str(a), str(b))
    return (answer, expression)
