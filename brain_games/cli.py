import prompt


def set_username():
    return prompt.string('May I have your name? ')


def welcome_user():
    user_name = set_username()
    print('Hello, {}!'.format(user_name))
