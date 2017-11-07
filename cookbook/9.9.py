# encoding=utf-8
# 将装饰器定义为类

from functools import wraps
import types


class Profile:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if not instance:
            return self
        else:
            return types.MethodType(self, instance)
