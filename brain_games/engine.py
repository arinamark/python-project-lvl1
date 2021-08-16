#!env python
from brain_games.cli import welcome_user
import prompt


def get_answer():
    return prompt.string('Your answer: ').rstrip().lower()


def ask_question(st):
    print('Question: {}'.format(st))


def gen_questions(func):
    (right, string) = func()
    ask_question(string)
    answer = get_answer()
    return (str(answer), str(right))


def show_win(name):
    print('Congratulations, {}!'.format(name))


def show_correct_stage():
    print('Correct!')


def show_loose(strings):
    (answers, name) = strings
    center_part = ' is wrong answer ;(. Correct answer was '
    st = '"{}"{}"{}".'.format(answers[0], center_part, answers[1])
    print(st)
    print('Let\'s try again, {}!'.format(name))


def stage_game(params):
    (answer, right, name, step) = params
    if (answer == right):
        if(step == 3):
            show_win(name)
            return 4
        else:
            show_correct_stage()
            return step + 1
    else:
        params2 = ((answer, right), name)
        show_loose(params2)
        return 4


def stages_logic(strings):
    (name, game) = strings
    step = 1
    while(step <= 3):
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
