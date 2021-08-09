from brain_games.games.even import even_ask
from brain_games.games.calc import calc_ask
from brain_games.games.gcd import gcd_ask


def gen_questions(game):
    if (game == 'calc'):
        (answer, right) = calc_ask()
    if (game == 'even'):
        (answer, right) = even_ask()
    if (game == 'gcd'):
        (answer, right) = gcd_ask()
    return (answer, right)
