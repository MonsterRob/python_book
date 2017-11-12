# encoding=utf-8
from inspect import getgeneratorstate
from functools import wraps


def simple_gen(a):
    print('--> coroutine started:', a)
    x = yield a
    print('--> coroutine received:', x)
    print('Die')


def coroutine(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return wrapper


@coroutine
def get_avg():
    total = 0.0
    count = 0
    average = None
    while True:
        number = yield average
        total += number
        count += 1
        average = total / count


my_cor = simple_gen(10)
x = next(my_cor)
print(x)
