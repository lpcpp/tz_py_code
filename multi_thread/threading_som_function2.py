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
        t.setDaemon(True)    # 守护线程，　设置主线程结束的时候，不用等待子线程结束, 如果不设置，默认为False
        t.start()

    for t in thread_list:
        # t.join()
        pass
    print threading.active_count()
    print 'major stop:', time.time()
