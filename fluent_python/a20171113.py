# encoding=utf-8
from collections import namedtuple


class Item:
    print('import doing the job item')

    def __init__(self, description, price, weigth):
        self.desciption = description
        self.price = price
        self.weight = weigth

    def subtotal(self):
        return self.price * self.weight

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError('value must be > 0')


class A(object):
    print('import doing the job A')

    def __init__(self, price, weight):
        self.price = price
        self.weigth = weight

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError('Value b=nust be > 0')
        self.__price = value

    price = property(fget=get_price, fset=set_price)


class B(object):
    name = 'xxx'

    def __init__(self, name):
        self.name = name


def quantity(storage_name):
    print('defination qty')

    def qty_get(instance):
        return instance.__dict__[storage_name]

    def qty_set(instance, value):
        if value < 0:
            raise ValueError('value must be > 0')
        instance.__dict__[storage_name] = value

    return property(fget=qty_get, fset=qty_set)


class C(object):
    def __init__(self, price):
        self.price = price


class D(object):
    name = 'xxx'

    def __getattr__(self, item):
        print(item, 'dddd')
        print('go here')


Cat = namedtuple('Cat', 'name age')
c = Cat('wali', 'eva')
print(c)
