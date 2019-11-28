# -*- coding:utf-8 -*-
# @Time : 2019/11/25 9:04 下午
# @Author: zhr619151879
# @File : Demo_thread.py

import random
import threading
import time


class DownLoadTask(threading.Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print(f'开始下载{self._filename}')
        time.sleep(1)
        time_for_download = random.randint(3,6)
        time.sleep(time_for_download)
        print(f'{self._filename} cost {time_for_download} seconds to complete with the task ')

if __name__ == '__main__':
    start = time.time()
    t1 = DownLoadTask('how to pass cet6?')
    t1.start()
    t2 = DownLoadTask("u need to calm down")
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print('process run %d seconds',start-end)