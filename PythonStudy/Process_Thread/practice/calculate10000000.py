# -*- coding:utf-8 -*-
# @Time : 2019/11/25 10:13 下午
# @Author: zhr619151879
# @File : calculate10000000.py

from multiprocessing import Process, Queue
import random
import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    start = time.time()
    print(f'i\'m creating list...')
    number_list = [x for x in range(1, 100000001)]
    print(f'it took {time.time()-start} seconds creating it')
    result_queue = Queue()
    index = 0

    for _ in range(8):
        print(f'i\'m splicing {_} and create process{_}! ')
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000],
                          result_queue))
        index += 12500000
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # calculate the total
    total = 0
    print('\n\ni\'m getting data from queue:')
    while not result_queue.empty():
        total += result_queue.get()
    print('Over!')
    print(total)


if __name__ == '__main__':
    main()
