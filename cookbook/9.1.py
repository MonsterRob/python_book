# encoding=utf-8
# 元编程解决代码重复问题
# 在函数上添加装饰器/包装器
# 函数的元信息
# 保留被装饰函数的元信息 functools.wraps
import time
from functools import wraps


def time_this(func):
    @wraps(func)  # 保留原始函数的元数据
    def wrapper(*args, **kwargs):
        s = time.time()
        rs = func(*args, **kwargs)
        e = time.time()
        print(e - s)
        return rs

    return wrapper


@time_this
def countdown(n: int):
    """
    Counts Down
    """
    while n:
        n -= 1


countdown(10000)
print(countdown.__name__, countdown.__doc__, countdown.__annotations__)
