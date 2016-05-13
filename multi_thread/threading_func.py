#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
利用threading模块新开线程, 传入一个函数对象到threading.Thread类中
"""
import time
import threading


sleep_time = [4, 6]


def foo(sec):
    print 'foo start:', time.time()    # 打印函数开始时间
    time.sleep(sec)
    print 'foo stop:', time.time()    # 打印函数结束时间


if __name__ == "__main__":
    print 'major start:', time.time()    # 打印主线程开始时间
    thread_list = []
    for sec in sleep_time:
        t = threading.Thread(target=foo, args=(sec,))    # 实例化线程, 在这里线程并没有启动
        thread_list.append(t)

    for t in thread_list:
        t.start()       # 启动线程

    for t in thread_list:
        t.join()       # 对子线程调用join操作，来确保子线程没有完全退出的时候，主线程阻塞在这里(在利用thread模块中我们需要使用锁来控制，可见threading模块的更方便之处)
    print 'major stop:', time.time()   # 打印主线程退出时间
