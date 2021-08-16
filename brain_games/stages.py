from brain_games.questions import gen_questions
from brain_games.cli import welcome_user


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


def barain_start(game):
    if (game == 'calc'):
        rule = 'What is the result of the expression?'
    if (game == 'even'):
        rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    if (game == 'gcd'):
        rule = 'Find the greatest common divisor of given numbers.'
    if (game == 'progression'):
        rule = 'What number is missing in the progression?'
    if (game == 'prime'):
        rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name = start_game(rule)
    relations = (name, game)
    stages_logic(relations)