# encoding=utf-8


class Quantity:
    _count = 0

    def __init__(self):
        self.storage_name = "{}#{}".format(self.__class__.__name__, self._count)
        self.__class__._count += 1

    # instance 托管实例
    def __set__(self, instance, value):
        print(instance, value)
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('Value must be > 0')

    def __get__(self, instance, owner):

        return instance.__dict__[self.storage_name]


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, desctiption, weight, price):
        self.description = desctiption
        self.price = price  # 触发__set__
        self.weight = weight

    # def __setattr__(self, key, value):
    #     print(key, value)

    def subtotal(self):
        return self.price * self.weight


if __name__ == '__main__':
    truffle = LineItem('white t', 100, 1)
    print(truffle.weight)
