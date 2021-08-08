from brain_games.cli import show_welcome, set_username
from brain_games.games.calc import calc_ask
from brain_games.games.even import even_ask


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
        if (game == 'calc'):
            (answer, right) = calc_ask()
        if (game == 'even'):
            (answer, right) = even_ask()
        relations = (answer, right, name, step)
        step = stage_game(relations)


def start_game(rule):
    name = set_username()
    show_welcome(name)
    print(rule)
    return name
