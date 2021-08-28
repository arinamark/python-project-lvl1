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
    expression = '{} + {}'.format(str(a), str(b))
    answer = a + b
    return (answer, expression)


def dev(a, b):
    expression = '{} - {}'.format(str(a), str(b))
    answer = a - b
    return (answer, expression)


def mul(a, b):
    expression = '{} * {}'.format(str(a), str(b))
    answer = a * b
    return (answer, expression)
