# -*- coding: utf-8 -*-


class MyCard:
    def __init__(self):
        self._cards = [1, 2, 3]
        self.name = 'xxx'

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        print(item)
        return self._cards[item]

    def __setitem__(self, key, value):
        if key > len(self._cards):
            print('wrong key')
            return
        self._cards[key] = value

    def __str__(self):
        return str(self._cards)

    def __getattr__(self, item):
        print(item, 'xxxx')

    def __getattribute__(self, item):
        print(item, 'zzzz')
        return 'wzz'

    def __setattr__(self, key, value):
        print(key, value)

    def __subclasscheck__(self, subclass):
        pass


def func(a: int, b: int) -> int:
    return a + b



c = MyCard()

print(c.name)
