# -*- coding:utf-8 -*-
# @Time : 2019/11/20 2:46 下午
# @Author: zhr619151879
# @File : Class_Design.py

class Chain(object):
    def __init__(self, path = ''):
        self._path = path



    def __getattr__(self, path):
        return Chain('%s/%s' %(self._path, path) )

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return  self._path

    __repr__ = __str__


print(Chain().users('michael').repos) # /users/michael/repos
print(Chain().users.michael.repos) # /users/michael/repos
