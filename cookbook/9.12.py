# -*- coding: utf-8 -*-
# 使用装饰器扩展类的功能
import sys


def log_getattribute(cls):
    origin_get = cls.__getattribute__

    def new_getattribute(self, name):
        print("Getting:", name)
        return origin_get(self, name)

    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


a = A(34)
print(a.x)
a.spam()
sys.stdout.write('hello world')

