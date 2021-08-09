#!env python
from random import randint
from math import gcd


def gen_expression():
    a = randint(0, 50)
    b = randint(0, 50)
    result = gcd(a, b)
    string = '{} {}'.format(str(a), str(b))
    return (result, string)
