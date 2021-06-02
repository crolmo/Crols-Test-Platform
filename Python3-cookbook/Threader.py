#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/5/14 10:41
# @Author : Crolmo
# @Site : 
# @File : Threader.py
# @Software: PyCharm

from threading import Thread


def sleep(time):
    print(time)
    import time
    time.sleep(5)


if __name__ == '__main__':
    import psutil
    for p in psutil.process_iter():
        print(p.cpu_times)
