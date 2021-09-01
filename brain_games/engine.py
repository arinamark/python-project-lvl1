#!env python
from brain_games.cli import welcome_user
import prompt


WIN_STEP = 3


def brain_start(rule, game_function):
    name = welcome_user()
    print(rule)
    step = 1
    while(step <= WIN_STEP):
        (right, expression) = game_function()
        print('Question: {}'.format(expression))
        answer = prompt.string('Your answer: ').rstrip().lower()
        if (answer == right):
            if(step == WIN_STEP):
                print('Congratulations, {}!'.format(name))
            else:
                print('Correct!')
        else:
            st = '{} is wrong answer ;(. Correct answer was {}.'.format(answer, right)
            print(st)
            print('Let\'s try again, {}!'.format(name))
            step = WIN_STEP
        step += 1
