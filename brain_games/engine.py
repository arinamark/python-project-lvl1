#!env python
from brain_games.cli import welcome_user
import prompt


WIN_STEP = 3


def brain_start(rule, game_function):
    name = start_game(rule)
    game(name, game_function)


def start_game(rule):
    name = welcome_user()
    print(rule)
    return name


def game(name, game_function):
    step = 1
    while(step <= WIN_STEP):
        (answer, right) = show_question(game_function)
        step = game_step(answer, right, name, step)


def show_question(game_function):
    (right, expression) = game_function()
    print('Question: {}'.format(expression))
    answer = prompt.string('Your answer: ').rstrip().lower()
    return (str(answer), str(right))


def game_step(answer, right, name, step):
    if (answer == right):
        if(step == WIN_STEP):
            print('Congratulations, {}!'.format(name))
            return WIN_STEP + 1
        else:
            print('Correct!')
            return step + 1
    else:
        show_loose(answer, right, name)
        return WIN_STEP + 1


def show_loose(wrong, right, name):
    st = '{} is wrong answer ;(. Correct answer was {}.'.format(wrong, right)
    print(st)
    print('Let\'s try again, {}!'.format(name))
