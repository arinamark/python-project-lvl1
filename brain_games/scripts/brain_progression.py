#!env python

from brain_games.engine import brain_start
from brain_games.games.progression import gen_expression


def main():
    brain_start('What number is missing in the progression?', gen_expression)


if __name__ == '__main__':
    main()
