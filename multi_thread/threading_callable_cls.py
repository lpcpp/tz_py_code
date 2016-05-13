#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
利用threading模块来创建线程，给threading.Thread传入一个可调用的类
"""
import time
import threading


sleep_time = [4, 6]


def foo(sec):
    print 'foo start:', time.time()    # 打印函数开始时间
    time.sleep(sec)
    print 'foo stop:', time.time()     # 打印函数结束时间


class ThreadFunc(object):          # 定义一个类
    def __init__(self, sec):
        self.sec = sec            # 初始化成员变量

    def __call__(self):          # 实现可调用的类的关键，定义一个__call__函数
        foo(self.sec)


if __name__ == "__main__":
    print 'major start:', time.time()    # 打印主线程开始时间
    thread_list = []
    for sec in sleep_time:
        t = threading.Thread(target=ThreadFunc(sec))     # 实例化线程对象，传入可调用的类
        thread_list.append(t)

    for t in thread_list:
        t.start()      # 开始线程

    for t in thread_list:
        t.join()       # 阻塞主线程
    print 'major stop:', time.time()   # 打印主线程退出时间
