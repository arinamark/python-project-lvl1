#!env python
from brain_games.games.stages import start_game, stages_logic


def calc_stage(name):
    relations = (name, 'calc')
    stages_logic(relations)


def start_calc():
    name = start_game('What is the result of the expression?')
    calc_stage(name)
