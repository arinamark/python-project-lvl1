#!env python


from random import randint
from brain_games.games.stages import stages_logic, start_game
from brain_games.games.questions import ask_question, get_answer


def if_even(number):
    return (number % 2 == 0)


def if_answer(params):
    (answer, correct) = params
    if(answer in ['yes', 'no']):
        return answer == correct
    return False


def gen_number(n):
    return randint(1, n)


def correct_answer(num):
    if if_even(num):
        return 'yes'
    return 'no'


def even_ask():
    number = gen_number(100)
    c_answer = correct_answer(number)
    ask_question(number)
    answer = get_answer()
    return (answer, c_answer)


def stage_even(name):
    relations = (name, 'even')
    stages_logic(relations)


def start_even():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    name = start_game(rule)
    stage_even(name)
