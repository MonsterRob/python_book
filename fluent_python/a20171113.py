# encoding=utf-8


class Item:
    def __init__(self, description, price, weigth):
        self.desciption = description
        self.price = price
        self.weight = weigth

    def subtotal(self):
        return self.price * self.weight

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError('value must be > 0')


item = Item('name', 0, 100)