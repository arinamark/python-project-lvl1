#!env python

import prompt
from brain_games.games.even import gen_expression as ask_even
from brain_games.games.calc import gen_expression as ask_calc
from brain_games.games.gcd import gen_expression as ask_gcd
from brain_games.games.progression import gen_expression as ask_progression
from brain_games.games.prime import gen_expression as ask_expression


def get_answer():
    return prompt.string('Your answer: ').rstrip().lower()


def ask_question(st):
    print('Question: {}'.format(st))


def gen_questions(game):
    if (game == 'calc'):
        (right, string) = ask_calc()
    if (game == 'even'):
        (right, string) = ask_even()
    if (game == 'gcd'):
        (right, string) = ask_gcd()
    if (game == 'progression'):
        (right, string) = ask_progression()
    if (game == 'prime'):
        (right, string) = ask_expression()
    ask_question(string)
    answer = get_answer()
    return (answer, right)
