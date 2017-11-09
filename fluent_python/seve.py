# -*- coding: utf-8 -*-

name = 10

print('defi outer name')


# 导入时运行

class A:
    print('defi name')
    name = 20

    # 导入时运行
    def say(self):
        # 调用时运行
        self.name = 10


def f():
    name = 10
    print(name)



