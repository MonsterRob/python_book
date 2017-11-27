# -*- coding: utf-8 -*-

class A:
    def __del__(self):
        print('gone')


a = A()
print('ddd')
