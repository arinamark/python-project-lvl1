#!env python
from brain_games.cli import welcome_user
import prompt


ANSWER_LABEL = 'Your answer: '
QUESTION_LABEL = 'Question:'
WIN_LABEL = 'Congratulations'
CORRECT_LABEL = 'Correct!'
WRONG_TEXT = ' is wrong answer ;(. Correct answer was '
TRY_TEXT = 'Let\'s try again'
WIN_STEP = 3


def gen_questions(func):
    (right, string) = func()
    print('{} {}'.format(QUESTION_LABEL, string))
    answer = prompt.string(ANSWER_LABEL).rstrip().lower()
    return (str(answer), str(right))


def show_loose(strings):
    (answers, name) = strings
    st = '"{}"{}"{}".'.format(answers[0], WRONG_TEXT, answers[1])
    print(st)
    print('{}, {}!'.format(TRY_TEXT, name))


def stage_game(params):
    (answer, right, name, step) = params
    if (answer == right):
        if(step == WIN_STEP):
            print('{}, {}!'.format(WIN_LABEL, name))
            return WIN_STEP + 1
        else:
            print(CORRECT_LABEL)
            return step + 1
    else:
        params2 = ((answer, right), name)
        show_loose(params2)
        return WIN_STEP + 1


def stages_logic(strings):
    (name, game) = strings
    step = 1
    while(step <= WIN_STEP):
        (answer, right) = gen_questions(game)
        relations = (answer, right, name, step)
        step = stage_game(relations)


def start_game(rule):
    name = welcome_user()
    print(rule)
    return name


def brain_start(rule, func):
    name = start_game(rule)
    relations = (name, func)
    stages_logic(relations)
