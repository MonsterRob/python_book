# -*- coding: utf-8 -*-
# 元编程技术 装饰器 元类


class Spam:
    def __init__(self, name):
        print('normal class')
        self.name = name


class NoInstance(type):
    def __call__(cls, *args, **kwargs):
        raise TypeError("Can't int")


class NoSpam(metaclass=NoInstance):
    @classmethod
    def just_say(cls):
        print('say class word')


class Singleton(type):
    # 初始化类
    def __init__(cls, *args, **kwargs):
        print('go here1')
        cls.__instance = None
        super().__init__(*args, **kwargs)

    # 调用类
    def __call__(cls, *args, **kwargs):
        print('go here2')
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class MySingleton(metaclass=Singleton):
    # 初始化实例
    def __init__(self, name):
        print('go here3')
        self.name = name



