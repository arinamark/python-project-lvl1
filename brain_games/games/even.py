#!env python
from random import randint


def gen_expression():
    number = randint(1, 100)
    if(number % 2 == 0):
        result = 'yes'
    else:
        result = 'no'
    return (result, str(number))
