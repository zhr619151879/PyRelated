# -*- coding:utf-8 -*-
# @Time : 2019/11/23 6:51 下午
# @Author: zhr619151879
# @File : 上下文管理器(with).py

class Test:
    def __enter__(self):
        print('enter')
        return [ i for i in range(1,10)]

    # 参数代表异常的种类、值、追踪信息(track_back)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self, exc_type, exc_val, exc_tb)
        import traceback
        print(traceback.extract_tb(exc_tb))
        print('exit')
        # 返回True则不会报错
        return True
with Test() as x:
    print('body:')
    print(x)
    1/0