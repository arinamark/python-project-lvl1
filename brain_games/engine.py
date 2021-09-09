#!env python
from brain_games.cli import welcome_user
import prompt


LAST_STEP = 3


def brain_start(rule, game_function):
    name = welcome_user()
    print(rule)
    step = 1
    while step <= LAST_STEP:
        (right, expression) = game_function()
        print('Question: {}'.format(expression))
        answer = prompt.string('Your answer: ').rstrip().lower()
        if answer == right:
            if step == LAST_STEP:
                print('Congratulations, {}!'.format(name))
            else:
                print('Correct!')
        else:
            loose_string = 'is wrong answer ;(. Correct answer was'
            st = '{} {} {}.'.format(answer, loose_string, right)
            print(st)
            print('Let\'s try again, {}!'.format(name))
            step = LAST_STEP
        step += 1
