# -*- coding: utf-8 -*-


class A:
    def __init__(self, x):
        self._x = x

    @classmethod
    def f(cls, name):
        print(cls, name)

    @staticmethod
    def sf():
        print('static')

    @classmethod
    def cf(*args):
        print(args)


class B:
    name = 10
    print(name)


class C(B):
    name = 20
    print(name)

    def say(self):
        pass


A.f('xxx')
a = A(1)
a.f('zzz')
a.sf()

b = A(2)
