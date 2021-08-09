#!env python
from random import randint
from math import gcd
from brain_games.games.questions import ask_question, get_answer


def gen_expression():
    a = randint(0, 50)
    b = randint(0, 50)
    result = gcd(a, b)
    string = '{} {}'.format(str(a), str(b))
    return (result, string)


def gcd_ask():
    (result, string) = gen_expression()
    ask_question(string)
    answer = get_answer()
    return (answer, str(result))
