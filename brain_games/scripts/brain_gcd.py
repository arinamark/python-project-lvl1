#!env python

from brain_games.engine import brain_start
from brain_games.games.gcd import gen_game_step, rule


def main():
    brain_start(rule, gen_game_step)


if __name__ == '__main__':
    main()
