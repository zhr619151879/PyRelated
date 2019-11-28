# -*- coding:utf-8 -*-
# @Time : 2019/11/25 3:32 下午
# @Author: zhr619151879
# @File : Demo_Process_comu.py

import multiprocessing
import os, time, random


def foo(aa):
    data = aa.get()
    print('receive data successfully!')
    print(f'data: {data}')


if __name__ == '__main__':
    tx = multiprocessing.Queue()  # 进程通信队列
    jc = multiprocessing.Process(target=foo, args=(tx,))  # 子进程
    print('parent ready to send data!')
    tx.put('有内鬼，终止交易！')
    jc.start()
    jc.join()
    print(f'data transmitted successfully!')
