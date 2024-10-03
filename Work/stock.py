from dataclasses import dataclass


# @dataclass
# class Stock:
#     name: str
#     shares: int
#     price: float

#     def cost(self):
#         return self.shares * self.price

#     def sell(self, x):
#         self.shares -= x


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, x):
        self.shares -= x


# a = Stock("GOOG", 100, 490.10)
