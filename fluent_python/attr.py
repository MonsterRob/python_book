# encoding=utf-8
# 属性 动态属性


class A:
    print('init class')
    age = 10

    def __init__(self, name):
        self.name = name

    # 获取不存在的属性才会调用
    # def __getattr__(self, item):
    #     print(item)
    #     return 'xxx'
    def __getattribute__(self, item):
        print('Getting:', item)
        return 'xxx'

    # 提供了__getattribute__ 则__getattr__不再使用
    def __getattr__(self, item):
        print('getting:', item)
        return 'ooo'


if __name__ == '__main__':
    a = A(name='xxx')
    print(a.age, a.name)
