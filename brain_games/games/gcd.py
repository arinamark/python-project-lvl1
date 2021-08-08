#!env python
from brain_games.games.stages import start_game, stages_logic


def gcd_stage(name):
    relations = (name, 'gcd')
    stages_logic(relations)


def start_gcd():
    name = start_game('Find the greatest common divisor of given numbers.')
    gcd_stage(name)
