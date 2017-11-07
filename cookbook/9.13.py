# -*- coding: utf-8 -*-
# 元编程技术 装饰器 元类


class Spam:
    def __init__(self, name):
        self.name = name


class NoInstance(type):
    def __call__(cls, *args, **kwargs):
        raise TypeError("Can't int")


class NoSpam(metaclass=NoInstance):
    @classmethod
    def just_say(cls):
        print('say class word')


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class MySingleton(metaclass=Singleton):
    def __init__(self, name):
        self.name = name


a = MySingleton('xxx')
b = MySingleton('zzz')

print(a is b, a.name, b.name)
