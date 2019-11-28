# -*- coding:utf-8 -*-
# @Time : 2019/11/18 3:26 下午
# @Author: zhr619151879
# @File : Decorator.py
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f'{text} {func.__name__}:')
            return func(*args, **kw)
        return wrapper
    return decorator