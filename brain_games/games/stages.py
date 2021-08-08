from brain_games.cli import show_welcome, set_username


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


def start_game(rule):
    name = set_username()
    show_welcome(name)
    print(rule)
    return name
