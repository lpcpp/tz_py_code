#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import thread


"""
利用thread模块来启动多个线程，该thread模块不推荐使用，建议使用threading模块，这里只是为了演示thread模块的用法
"""


def foo():
    print 'foo start:', time.time()   # 打印函数开始的时间
    time.sleep(4)                     # 函数睡眠4秒
    print 'foo stop:', time.time()    # 打印函数结束的时间


def bar():
    print 'bar start:', time.time()   # 打印函数开始的时间
    time.sleep(6)                     # 睡眠6秒
    print 'bar stop:', time.time()    # 打印函数结束的时间


if __name__ == "__main__":
    print time.time()                   # 打印主线程开始时间
    thread.start_new_thread(foo, ())    # 在主线程中开启一个线程
    thread.start_new_thread(bar, ())    # 在主线程中开启另一个线程
    time.sleep(10)                      # 为了保证子线程都执行完，主线程手动睡眠10秒,(非常笨的办法, 因为在实际清空中，我们并不知道子线程什么时候结束)
    print time.time()                   # 打印主线程退出时间
