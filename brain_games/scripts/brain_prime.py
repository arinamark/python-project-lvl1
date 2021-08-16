#!env python

from brain_games.engine import brain_start
from brain_games.games.prime import gen_expression


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brain_start(rule, gen_expression)


if __name__ == '__main__':
    main()
