# -*- coding:utf-8 -*-
# @Time : 2019/11/21 9:36 下午
# @Author: zhr619151879
# @File : ClassMethod.py

class Goods:
    __discount = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def change_discount(cls, new_discount):
        cls.__discount = new_discount

    @property
    def finally_price(self):
        return self.price * self.__discount

    @property
    def discount(self):
        return self.__discount

banana = Goods('香蕉', 10)
apple = Goods('苹果', 16)
Goods.change_discount(0.8)
print(f'{banana.discount}: {apple.discount}')
print(banana.finally_price)
print(apple.finally_price)

Goods.change_discount(0.5)
print(banana.finally_price)
print(apple.finally_price)