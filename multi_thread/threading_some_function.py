#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import threading


sleep_time = [4, 6]


def foo(sec):
    print 'foo start:', time.time()
    time.sleep(sec)
    print 'foo stop:', time.time()


class MyThread(threading.Thread):
    def __init__(self, sec):
        threading.Thread.__init__(self)
        self.sec = sec

    def run(self):
        foo(self.sec)


if __name__ == "__main__":
    print 'major start:', time.time()
    thread_list = []
    for sec in sleep_time:
        t = MyThread(sec)
        thread_list.append(t)

    for t in thread_list:
        t.start()
        print t.getName()      # 获取线程的名称
        t.setName('balala')    # 设置线程的名称
        print t.getName()
        print threading.enumerate()   # 获取所有的线程列表
        print threading.active_count()   # 获取活动的线程数量

    for t in thread_list:
        t.join()
    print 'major stop:', time.time()
