# -*- coding:utf-8 -*-
# @Time : 2019/11/22 10:14 上午
# @Author: zhr619151879
# @File : demo-1_file.py

"""
'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）
"""
import time


def method2():
    try:
        # 通过with关键字指定文件对象的上下文环境
        # 并在离开上下文环境时自动释放文件资源
        with open('text.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('can\'t open the specified file')
    except LookupError:
        print('an unknown code was specified')
    except UnicodeDecodeError:
        print('error coding while reading file')

def method3():
    # 一次性读取整个文件内容
    with open('text.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('text.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

if __name__ == '__main__':
    method3()
