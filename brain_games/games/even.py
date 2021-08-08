#!env python


from random import randint
from brain_games.games.stages import start_game
from brain_games.games.stages import show_loose, show_win, show_correct_stage
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


def game_stage(params):
    (step, name) = params
    number = gen_number(100)
    c_answer = correct_answer(number)
    ask_question(number)
    answers = (get_answer(), c_answer)
    if if_answer(answers):
        if(step == 3):
            show_win(name)
        else:
            show_correct_stage()
            params1 = (step + 1, name)
            game_stage(params1)
    else:
        params2 = (answers, name)
        show_loose(params2)


def start_even():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    name = start_game(rule)
    params = (1, name)
    game_stage(params)
