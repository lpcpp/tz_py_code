#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import thread
"""
使用thread模块, 加锁来控制主线程的退出
"""


sleep_time = [4, 6]     # 初始化一个全局列表，内容为线程的睡眠时间


def foo(sec, lock):    # 传入两个参数，　第一个参数为睡眠时间，第二个参数为锁
    print 'foo start:', time.time()     # 打印函数开始的时间
    time.sleep(sec)                     # 睡眠sec秒
    lock.release()                      # 释放锁
    print 'foo stop:', time.time()     # 打印函数结束的时间


if __name__ == "__main__":
    print time.time()       # 打印主线程开始的时间
    locks = []              # 初始化一个锁的列表
    for i in range(len(sleep_time)):
        lock = thread.allocate_lock()     # 新建一个锁
        lock.acquire()                    # 获得锁
        locks.append(lock)

    for i in range(len(sleep_time)):    # 开启的线程个数和sleep_time的长度一样
        thread.start_new_thread(foo, (sleep_time[i], locks[i]))    # 开启多个子线程

    while True:     # 写一个死循环，来不停的检测所有的锁有没有被释放掉
        for lock in locks:
            if lock.locked():     # 判断锁的状态
                pass
            else:
                locks.remove(lock)    # 如果锁的状态为unlock，那么从锁列表中移除
        if not locks:    # 如果所有的锁都被移除掉,那么break,主线程退出
            break

    print time.time()    # 打印主线程的退出时间
