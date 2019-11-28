# -*- coding:utf-8 -*-
# @Time : 2019/11/16 7:12 下午
# @Author: zhr619151879
# @File : First_class.py

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}', )

    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}只能观看《熊出没》')
        else:
            print('{}正在观看岛国爱情大电影!'.format(self.name))


if __name__ == '__main__':
    s1 = Student("木村扩哉", 18)
    s1.study('爱情是怎么炼成的')
    s1.watch_movie()

