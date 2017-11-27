# -*- coding: utf-8 -*-
import inspect


def fxu():
    return inspect.stack()[1]


print(fxu())
