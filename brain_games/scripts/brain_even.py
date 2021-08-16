#!env python

from brain_games.engine import brain_start
from brain_games.games.even import gen_expression


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    brain_start(rule, gen_expression)


if __name__ == '__main__':
    main()
