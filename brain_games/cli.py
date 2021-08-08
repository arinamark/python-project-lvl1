#!env python
import prompt


def set_username():
    return prompt.string('May I have your name? ')


def show_welcome(name):
    print('Hello, {}!'.format(name))


def welcome_user():
    user_name = set_username()
    show_welcome(user_name)
