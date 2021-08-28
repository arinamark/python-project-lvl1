#!env python
from random import randint


MAX_INT_FOR_RANDOM = 20
rule = 'What is the result of the expression?'


def get_result(params):
    (a, b, exp) = params
    if(exp == '+'):
        string = '{} + {}'.format(str(a), str(b))
        result = a + b
    if(exp == '-'):
        arg1 = max(a, b)
        arg2 = min(a, b)
        string = '{} - {}'.format(str(arg1), str(arg2))
        result = arg1 - arg2
    if(exp == '*'):
        string = '{} * {}'.format(str(a), str(b))
        result = a * b
    return (result, string)


def gen_expression():
    a = randint(0, MAX_INT_FOR_RANDOM)
    b = randint(0, MAX_INT_FOR_RANDOM)
    exp = ('+', '-', '*')[randint(0, 2)]
    params = (a, b, exp)
    return get_result(params)
