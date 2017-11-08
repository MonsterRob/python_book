# -*- coding: utf-8 -*-


class MyMeta(type):
    # 生成类
    def __new__(mcs, clsname, bases, clsdict):
        print(clsname, bases, clsdict)

        return super().__new__(mcs, clsname, bases, clsdict)

    # 实例化类
    def __init__(cls, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)


class Root(metaclass=MyMeta):
    pass


class A(Root, dict):
    def say(self):
        pass


class B(Root):
    pass
