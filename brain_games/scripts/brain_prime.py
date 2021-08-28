#!env python

from brain_games.engine import brain_start
from brain_games.games.prime import gen_expression, rule


def main():
    brain_start(rule, gen_expression)


if __name__ == '__main__':
    main()
