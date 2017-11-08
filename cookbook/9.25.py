# encoding=utf-8
# 拆解字解码
import dis


def count_down(n):
    while n:
        n -= 1
        print(n)
    else:
        print('blast_off')


print(count_down.__code__.co_code)
print(dis.dis(count_down))
