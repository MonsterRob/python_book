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


def e():
    yield from 'AB'
    yield from {1, 2, 3}


def f():
    def a():
        for b in range(3):
            yield b

    def g():
        for x in range(10):
            yield from a()

    def h():
        yield 'ABCD'

    yield from a()
    yield from g()
    yield from h()


print(list(f()))
