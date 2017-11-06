# -*- coding: utf-8 -*-
# 类支持比较操作 类装饰器

from functools import total_ordering


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.width * self.length


@total_ordering
class House:
    def __init__(self, age):
        self.age = age
        self.name = None
        self.style = None
        self.rooms = list()

    def __eq__(self, other):
        return self.age == other.age

    def __le__(self, other):
        return self.age < other.age


a = House(age=10)
b = House(age=30)
print(a != b)
