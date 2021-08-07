#!env python

from random import randint
import prompt
from brain_games.cli import set_username

def if_even(number):
    return (number % 2 == 0)
    

def gen_number(n):
    return randint(1,n)


def show_number(n):
    print('Question: {}'.format(n))


def show_win(name):
    print('Congratulations, {}!'.format(name))


def show_correct_stage():
    print('Correct!')


def show_loose(strings):
    (answers, name) = strings
    print('"{}" is wrong answer ;(. Correct answer was "{}".'.format(answers[0],answers[1]))
    print('Let\'s try again, {}!'.format(name))


def if_answer(params):
    (answer, correct) = params
    if(answer in ['yes','no']):
        return answer == correct
    return False 

def correct_answer(num):
    if if_even(num):
        return 'yes'
    return 'no'

def get_answer():
    return prompt.string('Your answer: ').rstrip().lower()

def game_stage(params):
    (step, name) = params
    number = gen_number(100)
    c_answer = correct_answer(number)
    show_number(number)
    answers = (get_answer(), c_answer)
    if if_answer(answers):
        if(step == 3):
            show_win(name)
        else:
            show_correct_stage()
            params1 = (step+1, name)
            game_stage(params1)
    else:
        params2 = (answers,name)
        show_loose(params2)
        game_stage((1, name))

def start_game():
    name = set_username()
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    params = (1, name)
    game_stage(params)
