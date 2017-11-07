# -*- coding: utf-8 -*-
# 给类或者静态方法提供装饰器
from functools import wraps
import time


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = time.time()
        rs = func(*args, **kwargs)
        e = time.time()
        print(e - s)
        return rs

    return wrapper


class MyClass:
    @time_this
    def say_hello(self):
        print('instance say hello')

    @classmethod
    @time_this
    def say_1(cls):
        print('cls say hello')
