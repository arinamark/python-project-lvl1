#!env python
from random import randint


MAX_INT_FOR_RANDOM = 20
rule = 'What is the result of the expression?'


def gen_expression():
    a = randint(0, MAX_INT_FOR_RANDOM)
    b = randint(0, MAX_INT_FOR_RANDOM)
    operator = ('+', '-', '*')[randint(0, 2)]
    expression = (a, b, operator)
    return get_correct_answer(expression)


def get_correct_answer(expression):
    (a, b, operator) = expression
    if(operator == '+'):
        return add(a, b)
    if(operator == '-'):
        argument1 = max(a, b)
        argument2 = min(a, b)
        return dev(argument1, argument2)
    if(operator == '*'):
        return mul(a, b)


def add(a, b):
    string = '{} + {}'.format(str(a), str(b))
    result = a + b
    return (result, string)


def dev(a, b):
    string = '{} - {}'.format(str(a), str(b))
    result = a - b
    return (result, string)


def mul(a, b):
    string = '{} * {}'.format(str(a), str(b))
    result = a * b
    return (result, string)
