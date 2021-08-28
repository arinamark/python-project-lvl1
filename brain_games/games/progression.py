#!env python
from random import randint


GEN_P_LENGTH_MIN = 5
GEN_P_LENGTH_MAX = 10
GEN_START_NUMBER = 10
GEN_STEP = 10
rule = 'What number is missing in the progression?'


def gen_expression():
    p_lenth = randint(GEN_P_LENGTH_MIN, GEN_P_LENGTH_MAX)
    p_start = randint(1, GEN_START_NUMBER)
    p_step = randint(1, GEN_STEP)
    p_index = randint(0, p_lenth - 1)
    progression = []
    i = 0
    element = p_start
    while (i < p_lenth):
        if (i == p_index):
            result = element
            progression.append('..')
        else:
            progression.append(str(element))
        i = i + 1
        element = element + p_step
    string = ' '.join(progression)
    return (result, string)
