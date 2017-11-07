# -*- coding: utf-8 -*-
# 装饰器为被包装函数增加参数
from functools import wraps


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def my_f(a, b, c):
    print(a, b, c)


my_f(1, 2, 3, debug=True)
