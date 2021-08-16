#!env python
from random import randint
from math import gcd


GEN_GCD = 50


def gen_expression():
    a = randint(0, GEN_GCD)
    b = randint(0, GEN_GCD)
    result = gcd(a, b)
    string = '{} {}'.format(str(a), str(b))
    return (result, string)
