# -*- coding:utf-8 -*-
# @Time : 2019/11/25 1:47 下午
# @Author: zhr619151879
# @File : Demo_Process.py

import multiprocessing
import time


def action(a, b):  # 待会两个进程要执行的任务↓
    for i in range(10):  # 循环30次
        print(a, ' ', b)
        time.sleep(0.5)  # 等待0.1s


if __name__ == '__main__':
    jc1 = multiprocessing.Process(target=action, args=('进程一', 0))
    jc2 = multiprocessing.Process(target=action, args=('进程二', 1))
    # target:指定进程要执行的任务(这里是执行函数 action)
    # args:target的参数即action的参数，是元组，所以args的\参数写成tuple格式
    jc1.start()
    jc2.start()
    jc1.join()
    jc2.join()
    print('task is over!')
    jc1.close()
    jc2.close()
