from brain_games.games.question_even import even_ask
from brain_games.games.question_calc import calc_ask
from brain_games.games.question_gcd import gcd_ask


def gen_questions(game):
    if (game == 'calc'):
        (answer, right) = calc_ask()
    if (game == 'even'):
        (answer, right) = even_ask()
    if (game == 'gcd'):
        (answer, right) = gcd_ask()
    return (answer, right)
