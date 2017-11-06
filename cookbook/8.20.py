# -*- coding: utf-8 -*-
# 通过字符串调用方法
import math
import operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(4, 3)
# d = getattr(p, 'distance')(0, 0)
# print(d)
# print(Point.__dict__)

d = operator.methodcaller('distance', 0, 0)
print(d(p))

