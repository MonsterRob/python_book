# -*- coding: utf-8 -*-
# 在类中定义装饰器
from functools import wraps


class A:
    def deco1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('instance deco')
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def deco2(cls, func):
        @wraps(func)
        def wraaper(*args, **kwargs):
            print('class deco')
            return func(*args, **kwargs)

        return wraaper


a = A()


@a.deco1
def myf():
    print('say hello')


myf()


@A.deco2
def myff():
    print('say class hello')


myff()
