#!env python
from random import randint


GEN_NUMBER = 100


def gen_expression():
    number = randint(1, GEN_NUMBER)
    if(number % 2 == 0):
        result = 'yes'
    else:
        result = 'no'
    return (result, str(number))
