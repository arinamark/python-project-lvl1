#!env python

import prompt


def get_answer():
    return prompt.string('Your answer: ').rstrip().lower()


def ask_question(st):
    print('Question: {}'.format(st))
