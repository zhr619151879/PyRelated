import multiprocessing
import time, os, random

def action1(a, b=20):
    for i in range(b):
        print(a, os.getpid(), ' ', i)
        time.sleep(0.1)

if __name__ == '__main__':
    # create a processes pool, capacity is 3
    p = multiprocessing.Pool(3)
    p.apply_async(action1, args=('Process 1',))
    p.apply_async(action1, args=('Process 2', 10))
    p.apply_async(action1, args=('Process 3', 15))

    p.close() #关闭进程池 但池子内已启动的子进程仍会进行
    p.join()
    print('end!')
