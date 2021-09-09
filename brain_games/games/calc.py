#!env python
from random import randint


MAX_INT_FOR_RANDOM = 20
rule = 'What is the result of the expression?'


def gen_game_step():
    a = randint(0, MAX_INT_FOR_RANDOM)
    b = randint(0, MAX_INT_FOR_RANDOM)
    operator = ('+', '-', '*')[randint(0, 2)]
    expression = (a, b, operator)
    return get_step(expression)


def get_step(expression):
    a, b, operator = expression
    if operator == '+':
        return get_step_add(a, b)
    if operator == '-':
        argument1 = max(a, b)
        argument2 = min(a, b)
        return get_step_sub(argument1, argument2)
    if operator == '*':
        return get_step_mul(a, b)


def get_step_add(a, b):
    expression = '{} + {}'.format(str(a), str(b))
    answer = a + b
    return str(answer), expression


def get_step_sub(a, b):
    expression = '{} - {}'.format(str(a), str(b))
    answer = a - b
    return str(answer), expression


def get_step_mul(a, b):
    expression = '{} * {}'.format(str(a), str(b))
    answer = a * b
    return str(answer), expression
