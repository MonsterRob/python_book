# encoding=utf-8
# 拆解字解码
import dis
from collections import Iterable


def count_down(n):
    while n:
        n -= 1
        print(n)
    else:
        print('blast_off')


def plain_list(ls):
    rl = []
    for x in ls:
        if not isinstance(x, Iterable):
            pass
