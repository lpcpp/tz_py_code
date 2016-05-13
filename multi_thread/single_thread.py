#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
单线程顺序执行两个独立的函数
"""
import time


def foo():
    time.sleep(4)     # 睡眠4秒


def bar():
    time.sleep(6)     # 睡眠6秒


if __name__ == "__main__":
    print time.time()      # 打印主线程开始的时间
    foo()                  # 调用foo函数
    bar()                  # 调用bar函数
    print time.time()      # 打印主线程结束的时间
