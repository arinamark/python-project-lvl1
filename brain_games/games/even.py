#!env python
from brain_games.games.stages import stages_logic, start_game


def stage_even(name):
    relations = (name, 'even')
    stages_logic(relations)


def start_even():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    name = start_game(rule)
    stage_even(name)
