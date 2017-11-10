# -*- coding: utf-8 -*-


def fib(n):
    a, b, = 0, 1
    while b < n:
        yield b
        a, b = b, a + b


def my_chain(*iterables):
    for it in iterables:

        yield from it
        print('xxx')


a = "ABC"
b = tuple(range(3))

c = my_chain(a, b)
print('xxx')

