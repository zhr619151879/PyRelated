# -*- coding:utf-8 -*-
# @Time : 2019/11/24 8:47 下午
# @Author: zhr619151879
# @File : create_new_file.py

import os

def create_new_file(file_name):
    # cur_path = os.path.abspath('.')
    target_path = os.path.join(file_name)
    os.mkdir(target_path)
    # os.rmdir(target_path)

def split_file(path = None):
    cur_path = os.getcwd()
    print(cur_path)
    # res = os.path.split(cur_path)
    res = os.path.splitext(cur_path)
    return res


print(split_file())

