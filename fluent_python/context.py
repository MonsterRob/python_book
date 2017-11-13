# encoding=utf-8
from contextlib import contextmanager


@contextmanager
def mygen():
    name = 'xxx'
    yield name
    print('Go out')


with mygen() as n:
    print('inner')
    print(n)

    # 三段式 enter with exit
