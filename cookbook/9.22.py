# encoding=utf-8
# 定义上下文管理器
import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    s = time.time()
    print('before')
    try:
        yield  # 执行分割线
    finally:
        e = time.time()
        print('down')
        print("{}:{}".format(label, e - s))


with timethis('Counting'):
    n = 1000000
    while n:
        n -= 1
