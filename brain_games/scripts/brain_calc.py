#!env python

from brain_games.engine import brain_start
from brain_games.games.calc import gen_expression


def main():
    brain_start('What is the result of the expression?', gen_expression)


if __name__ == '__main__':
    main()
