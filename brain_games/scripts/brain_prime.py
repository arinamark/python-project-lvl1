#!env python

from brain_games.engine import brain_start
from brain_games.games.prime import gen_expression


def main():
    brain_start('Answer "yes" if given number is prime. Otherwise answer "no".', gen_expression)


if __name__ == '__main__':
    main()
