# encoding=utf-8
class A:
    def __init__(self, x):
        self.x = x

    def __bool__(self):
        return bool(self.x)

    def __subclasscheck__(self, subclass):
        return True


class B:
    def __subclasscheck__(self, subclass):
        print(subclass)
        return True


print(issubclass(A, B))
