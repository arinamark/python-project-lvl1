#!env python
from random import randint, choice
from operator import add, mul, sub


MAX_INT_FOR_RANDOM = 20
rule = 'What is the result of the expression?'


def gen_game_step():
    a = randint(0, MAX_INT_FOR_RANDOM)
    b = randint(0, MAX_INT_FOR_RANDOM)
    operator = choice(['+', '-', '*'])
    question = a, b, operator
    return get_step(question)


def get_step(question):
    a, b, operator = question
    if operator == '+':
        operation = add
    if operator == '-':
        a = max(a, b)
        b = min(a, b)
        operation = sub
    if operator == '*':
        operation = mul
    return str(operation(a, b)), '{} {} {}'.format(a, operator, b)
