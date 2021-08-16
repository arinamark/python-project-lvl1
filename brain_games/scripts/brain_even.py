#!env python

from brain_games.engine import brain_start
from brain_games.games.even import gen_expression


def main():
    brain_start('Answer "yes" if the number is even, otherwise answer "no".', gen_expression)


if __name__ == '__main__':
    main()
