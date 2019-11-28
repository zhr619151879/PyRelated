# -*- coding:utf-8 -*-
# @Time : 2019/11/22 9:01 下午
# @Author: zhr619151879
# @File : Json.py

import json

"""dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象"""

def main():
    mydict = {
        'name' : '超梦',
        'age' : 21,
        'qq' : 123455,
        'friends' : ['喷火龙', '蒜头王八'],
        'cars' : [
            {'brand' : 'BYD', 'max_speed': 180},
            {'brand' : 'Audi', 'max_speed': 280},
            {'brand' : 'Benz', 'max_speed': 320}
        ]
    }
    try:
        # with open('data.json', 'w', encoding='utf-8') as f:
        #     json.dump(mydict, f)
        str = json.dumps(mydict)
        print(str)
    except IOError as e:
        print(e)
    print('保存数据完成!')

if __name__ == '__main__':
    main()