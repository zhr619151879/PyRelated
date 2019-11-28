# -*- coding:utf-8 -*-
# @Time : 2019/11/20 4:15 下午
# @Author: zhr619151879
# @File : Enumerate.py

from enum import Enum, unique


@unique  # 防止值不唯一
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(dir(Weekday.Fri))
print(Weekday.Fri.name)
print(Weekday.Fri.value)
print(Weekday(4).name)