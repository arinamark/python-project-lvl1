#!env python
from random import randint


MAX_NUMBER_FOR_RANDOM = 100
rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def gen_expression():
    number = randint(1, MAX_NUMBER_FOR_RANDOM)
    if(number % 2 == 0):
        answer = 'yes'
    else:
        answer = 'no'
    return (answer, str(number))
