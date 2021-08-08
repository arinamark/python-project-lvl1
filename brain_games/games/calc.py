#!env python

from random import randint
from brain_games.games.stages import show_correct_stage, show_loose, show_win, start_game
from brain_games.games.questions import ask_question, get_answer

def gen_expression():
    a = randint(0, 100)
    b = randint(0, 100)
    exp = ('+', '-', '*')[randint(0, 2)]
    return '{} {} {}'.format(str(a), exp, str(b))


def calc_stage(params):
    ask_question(gen_expression())
    answer = get_answer()
    return False


def start_calc():
    name = start_game('What is the result of the expression?')
    params = (1, name)
    calc_stage(params)
