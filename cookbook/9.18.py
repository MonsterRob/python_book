# encoding=utf-8
import types


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


clsdict = {
    '__init__': __init__,
    'cost': cost
}
Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(clsdict))
Stock.__module__ = __name__

print(Stock)
