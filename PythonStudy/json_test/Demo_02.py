# -*- coding:utf-8 -*-
# @Time : 2019/11/24 9:19 下午
# @Author: zhr619151879
# @File : Demo_02.py

from io import StringIO
import json

io = StringIO()
json.dump([1, 2, 3, {'4': 5, '6': 7}], io,
          separators=(',', ':'))
print(io.getvalue())
print(json.loads(io.getvalue()))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def student2dict(self):
        return{
            'name': self.name,
            'age' : self.age,
            'score': self.score
        }

# 参数ensure_ascii=False 才会输出中文
s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))
print(json.dumps(s.__dict__))
