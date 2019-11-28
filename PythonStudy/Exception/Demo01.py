# -*- coding:utf-8 -*-
# @Time : 2019/11/23 6:29 下午
# @Author: zhr619151879
# @File : Demo01.py
# 简单的异常处理

def try_01():
    try:
        print(name)
        print(1/0)
    except (ZeroDivisionError, NameError) as e:
        print('exception:', e)


def try_02():
    try:
        f = open('notExistFile','r')
    except Exception as e :
        print(f'error {e}')

