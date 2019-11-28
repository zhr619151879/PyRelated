# -*- coding:utf-8 -*-
# @Time : 2019/11/22 11:26 上午
# @Author: zhr619151879
# @File : Read_binary.py

"""复制图片文件"""

#用 yield实现文件读取
def read_file(path):
    BLOCK_SIZE = 1024
    with open(path, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('copy.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')

main()