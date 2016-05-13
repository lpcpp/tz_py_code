#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
使用threading模块，通过继承threading.Thread类来实现线程的创建
"""
import time
import threading


sleep_time = [4, 6]


def foo(sec):
    print 'foo start:', time.time()
    time.sleep(sec)
    print 'foo stop:', time.time()


class MyThread(threading.Thread):    # 定义一个类，继承threading.Thread
    def __init__(self, sec):
        threading.Thread.__init__(self)    # 调用父类的初始化函数
        self.sec = sec              # 初始化成员变量

    def run(self):                # 复写run方法，线程的所有逻辑都放在run方法里面
        foo(self.sec)


if __name__ == "__main__":
    print 'major start:', time.time()   # 打印主线程开始时间
    thread_list = []
    for sec in sleep_time:
        t = MyThread(sec)     # 实例化线程类
        thread_list.append(t)

    for t in thread_list:
        t.start()            # 线程开始

    for t in thread_list:
        t.join()          # 阻塞父线程，直到所有的子线程退出
    print 'major stop:', time.time()    # 打印主线程结束时间
