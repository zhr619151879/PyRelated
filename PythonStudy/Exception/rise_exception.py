# -*- coding:utf-8 -*-
# @Time : 2019/11/23 7:59 下午
# @Author: zhr619151879
# @File : rise_exception.py

class Age_exception(Exception):
    def __init__(self, msg, error_code):
        self.msg = msg
        self.error_code = error_code

    def __str__(self):
        return f'{self.msg},code:{self.error_code}'

def set_age(age):
    if (age < 0):
        raise  Age_exception('年龄要大于0!', 404)

    else:
        print(f'设定年龄为{age}成功!')

def test_set():
    try:
        set_age(-2)
    except Age_exception as e:
        print('wrong!')
        raise
