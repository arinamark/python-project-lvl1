from random import randint
from brain_games.games.questions import ask_question, get_answer


def even_ask():
    number = randint(1, 100)
    if(number % 2 == 0):
        c_answer = 'yes'
    else:
        c_answer = 'no'
    ask_question(str(number))
    answer = get_answer()
    return (answer, c_answer)
