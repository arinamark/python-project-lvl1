#!env python
from random import randint


def gen_expression():
    p_lenth = randint(5, 10)
    p_start = randint(1, 10)
    p_step = randint(1, 10)
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
