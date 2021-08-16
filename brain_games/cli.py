#!env python
import prompt


NAME_ASK_LABEL = 'May I have your name? '
WELCOME_LABEL = 'Hello'
START_TEXT = 'Welcome to the Brain Games!'


def set_username():
    return prompt.string(NAME_ASK_LABEL)


def welcome_user():
    print(START_TEXT)
    user_name = set_username()
    print('{}, {}!'.format(WELCOME_LABEL, user_name))
    return user_name
