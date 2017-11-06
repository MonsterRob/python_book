# encoding=utf-8
from abc import ABCMeta, abstractmethod
from collections import Iterable
import time


def description():
    """
    8.6 创建可管理的属性 属性检查
    8.7 调用父类的方法 super() 涉及到多继承时 使用super函数 C3线性化算法 算法的数学原理
    8.8 子类中扩展父类的属性
    8.9 创建新的类或者实例属性 描述器
    8.11 简化数据结构的初始化 在基类中写init函数 实例字典 类字典
    8.12 抽象基类 用来定义接口 检查子类实现情况 强制类型检查减少了代码的灵活性
    8.13
    8.14 实现自定义容器 基本不会出现
    8.15 代理对象
    8.16 定义多个构造器
    8.17 创建不用调用__init__()的实例
    8.18 扩展其他类的功能 ：功能准备 扩展类选择

    """
    pass


class Person(object):
    def __init__(self, f_name):
        self._f_name = f_name

    @property
    def f_name(self):
        return self.f_name

    @f_name.setter
    def f_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expect a string')
        self._f_name = value

    @f_name.deleter
    def f_name(self):
        raise AttributeError("Can't delete")

    def __setattr__(self, key, value):
        print('go hear')
        object.__setattr__(self, key, value)


class SubPerson(Person):
    pass


class A(object):
    def __init__(self, x=0):
        self.x = 0


class B(A):
    def __init__(self, y):
        super().__init__()
        self.y = y


class Integer(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(instance)
        if not isinstance(value, int):
            raise TypeError('Int required')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point(object):
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class SuperStructure(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(self._fields) != len(args):
            raise TypeError('expect {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
            # self.__dict__.update(zip(self._fields, args))
            # self.__dict__.update(kwargs)


class Stock(SuperStructure):
    _fields = ['name', 'age']


class IStream(metaclass=ABCMeta):
    pass


class AA(Iterable):
    def __iter__(self):
        pass


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        print('init')

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)  # 会调用init方法


class LoggedMappingMixin(object):
    __slots__ = ()

    pass


if __name__ == '__main__':
    b = Date.today()
