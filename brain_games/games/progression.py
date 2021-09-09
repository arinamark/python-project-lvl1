#!env python
from random import randint


PROGRESSION_LENGTH_MIN = 5
PROGRESSIN_LENGTH_MAX = 10
START_NUMBER = 10
STEP = 10
rule = 'What number is missing in the progression?'


def gen_game_step():
    progression = progression_generate()
    answer_index = randint(0, len(progression) - 1)
    answer = progression[answer_index]
    question = str_progression(progression, answer_index)
    return str(answer), question


def progression_generate():
    length = randint(PROGRESSION_LENGTH_MIN, PROGRESSIN_LENGTH_MAX)
    start = randint(1, START_NUMBER)
    step = randint(1, STEP)
    end = start + step * length
    return [*range(start, end, step)]


def str_progression(prorgression, index):
    expression = []
    for i, element in enumerate(prorgression):
        if i == index:
            expression.append('..')
        else:
            expression.append(str(element))
    return ' '.join(expression)
