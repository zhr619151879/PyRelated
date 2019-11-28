import multiprocessing
import time


def foo(i):
    time.sleep(2)
    return i + 100


def bar(arg):
    print('-->exec done: ', arg)


pool = multiprocessing.Pool(5)

# 由于进程池只设置了5个，所以只会加入5个进程入队列
# 剩下的都被挂起等待
for i in range(10):
    pool.apply_async(func=foo, args=(i,), callback=bar)

print('end')
pool.close()
pool.join()
