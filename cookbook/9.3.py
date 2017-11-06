# encoding=utf-8
# 定义一个带参数的装饰器
# 两步调用 先调用含参外部函数 在调用被装饰函数
from functools import wraps


def logged(level, name=None, message=None):
    def dec(func):
        print(level, name, message)

        # 因为内部有引用 level name message 不会销毁
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        return inner

    return dec
