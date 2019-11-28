# -*- coding:utf-8 -*-
# @Time : 2019/11/25 9:25 下午
# @Author: zhr619151879
# @File : Demo_thread_lock.py

import time
import threading

# 设想用多个线程对一个账户同时存入1元
# 那么该账户则成为了共享的资源，需要加锁保护
class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = threading.Lock()

    def deposit(self, money):
        #obtain the lock before executing the code
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            time.sleep(0.01)
            self._balance = new_balance
        finally:
            # release the lock
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(threading.Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f'the balance of account is : {account.balance}')

if __name__ == '__main__':
    main()