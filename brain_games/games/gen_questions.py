from random import randint
from brain_games.games.questions import ask_question, get_answer
from brain_games.games.question_even import even_ask


def get_result(params):
    (a, b, exp) = params
    if(exp == '+'):
        string = '{} + {}'.format(str(a), str(b))
        result = a + b
    if(exp == '-'):
        arg1 = max(a, b)
        arg2 = min(a, b)
        string = '{} - {}'.format(str(arg1), str(arg2))
        result = arg1 - arg2
    if(exp == '*'):
        string = '{} * {}'.format(str(a), str(b))
        result = a * b
    return (result, string)


def gen_expression():
    a = randint(0, 100)
    b = randint(0, 100)
    exp = ('+', '-', '*')[randint(0, 2)]
    params = (a, b, exp)
    return get_result(params)


def calc_ask():
    (result, string) = gen_expression()
    ask_question(string)
    answer = get_answer()
    return (answer, str(result))


def gen_questions(game):
    if (game == 'calc'):
        (answer, right) = calc_ask()
    if (game == 'even'):
        (answer, right) = even_ask()
    return (answer, right)
