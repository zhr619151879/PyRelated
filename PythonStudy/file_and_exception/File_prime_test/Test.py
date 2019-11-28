# -*- coding:utf-8 -*-
# @Time : 2019/11/22 10:45 上午
# @Author: zhr619151879
# @File : Test.py

import math

"""在1-9999间的素数写在三个文件中
1-99之间的素数保存在a.txt中
100-999之间的素数保存在b.txt中
1000-9999之间的素数保存在c.txt中）"""

def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True if n != 1 else False

def write_prime():
    file_names = ['a.txt','b.txt','c.txt']
    file_list = [ open( file_names[i], mode='w',encoding='utf-8') for i in range(0,len(file_names))]
    # print(file_list)
    for i in file_list:
        print(i)
    for i in range(1,10000):
        if(is_prime(i)):
            if (i < 100):
                file_list[0].write(str(i)+'\n')
            elif(i<1000):
                file_list[1].write(str(i) + '\n')
            else:
                file_list[2].write(str(i) + '\n')

if __name__ == '__main__':
    write_prime()