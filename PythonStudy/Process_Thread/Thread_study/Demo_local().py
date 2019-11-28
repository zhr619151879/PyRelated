import time, threading
#解决了一个线程中各个函数之间传递的问题

# 全局变量local_school就是一个ThreadLocal对象
# 每个Thread对它都可以读写student属性，但互不影响
# 你可以把local_school看成全局变量
# 但每个属性如local_school.student都是线程的局部变量
# 可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理
# 可以理解为是一个dict{线程名:属性}

# create global *ThreadLocal* object
local_school = threading.local()


def process_thread(name):
    # bind student with ThreadLocal
    local_school.std_name = name
    process_student()

def process_student():
    # Gets the current thread related student
    std = local_school.std_name
    print(f'Hello, this is {std} in thread:' \
          f' {threading.current_thread().name}')


if __name__ == '__main__':
    t1 = threading.Thread(
        target=process_thread, args=('喷火龙',), name='thread1')
    t2 = threading.Thread(
        target=process_thread, args=('水箭龟',), name='thread2')
    t3 = threading.Thread(
        target=process_thread, args=('妙蛙花',), name='thread3')
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
