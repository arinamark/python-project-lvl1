#!env python

from random import randint
from brain_games.games.stages import start_game, stages_logic
from brain_games.games.questions import ask_question, get_answer


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
    a = randint(0, 100)
    b = randint(0, 100)
    exp = ('+', '-', '*')[randint(0, 2)]
    params = (a, b, exp)
    return get_result(params)


def calc_ask():
    (result, string) = gen_expression()
    ask_question(string)
    answer = get_answer()
    return (answer, str(result))


def calc_stage(name):
    relations = (name, 'calc')
    stages_logic(relations)


def start_calc():
    name = start_game('What is the result of the expression?')
    calc_stage(name)
