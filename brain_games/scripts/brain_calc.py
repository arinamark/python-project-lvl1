#!env python

from brain_games.engine import game
from brain_games.games.calc import gen_game_step, rule


def main():
    game(rule, gen_game_step)


if __name__ == '__main__':
    main()
