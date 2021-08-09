#!env python
from random import randint


def is_prime(num):
    if ((num == 1) or (num == 2)):
        return 'yes'
    else:
        dev = 2
        while(dev < num):
            if (num % dev == 0):
                return 'no'
            dev = dev + 1
        return 'yes'


def gen_expression():
    a = randint(1, 100)
    result = is_prime(a)
    return (result, str(a))
