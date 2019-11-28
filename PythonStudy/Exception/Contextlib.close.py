# -*- coding:utf-8 -*-
# @Time : 2019/11/23 7:24 下午
# @Author: zhr619151879
# @File : Contextlib.close.py

import contextlib
class Test(object):
    def exec(self):
        print('do something.....')

    def close(self):
        print('must be executed...')
        print('Release resource...')

with contextlib.closing(Test()) as obj_test:
    obj_test.exec()
    print(f'doing more thing...')