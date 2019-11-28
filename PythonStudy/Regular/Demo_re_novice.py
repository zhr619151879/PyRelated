# -*- coding:utf-8 -*-
# @Time : 2019/11/27 9:26 下午
# @Author: zhr619151879
# @Keymap: 「command+1:surround command+p:parameter ctr+o overide」
# @File : Demo_re_novice.py

import re


def method1_match():
    # match 方法判断是否匹配，如果匹配成功返回一个Match对象
    # 否则返回 None
    # pattern为 三个数字 - （3-8）个数字
    pat = r'^\d{3}\-\d{3,8}$'
    s = r'010-001'

    def matchit(pattern, str):
        print('pattern: ', pattern)
        print('string: ', str)
        if re.match(pattern, str):
            print('cool~')
        else:
            print('no!')

    matchit(pat, s)


def method2_split():
    # 可以连续捕捉空格等符号来分割
    # print(re.split(r'\s+', 'a,b, c      d'))
    print(re.split(r'[\s\,\;]+', 'a,b,;; c      d'))


def method3_group():
    # 正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组
    # ^(\d{3})-(\d{3,8})$ 便定义了两个组

    # 识别时间
    p = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])' \
        r'\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])' \
        r'\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$'
    s = '19:05:30'
    m = re.match(p, s)
    print(m.groups())  # group(0)是原字符串


def greed_match():
    # 正则匹配默认是贪婪匹配
    # 如 r'^(\d+)(0*)$' 去匹配(102300)
    # 结果是 ('1023', '')
    # 因为(\d+)采用贪婪匹配,直接把后面的0匹配了.(0*+)只能匹配空字符串了
    res = re.match(r'^(\d+?)(0*)$', '102300')
    print(res.groups())  # ('1023', '00')

def compile_first():
    # 如果一个正则表达式需要重复使用N次
    # 出于对效率的考虑,可以预编译该表达式
    pattern = r'^(\d{3})\-(\d{3,8})$'
    re_precompile = re.compile(pattern)
    print(re_precompile.match('010-12345').groups())

method1_match()
method3_group()
greed_match()
compile_first()