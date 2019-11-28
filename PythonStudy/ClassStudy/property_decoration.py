# -*- coding:utf-8 -*-
# @Time : 2019/11/17 9:53 上午
# @Author: zhr619151879
# @File : property_decoration.py


class Person(object):

    __slots__ = ('name', 'age', 'gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name} is playing soil~')
        else:
            print(f'{self._name} is sucking~')

if __name__ == '__main__':
    person = Person('皮卡丘',12)
    person.play()
    person.age = 22
    person.play()
    print((person.name))
    # person._Person_name = 'ss'