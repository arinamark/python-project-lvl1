#!env python

from brain_games.engine import brain_start
from brain_games.games.gcd import gen_expression


def main():
    brain_start('Find the greatest common divisor of given numbers.', gen_expression)


if __name__ == '__main__':
    main()
