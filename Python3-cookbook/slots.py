#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/27 13:32
# @Author : Crolmo
# @Site : 
# @File : slots.py
# @Software: PyCharm
import sys


class slotsdemo:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day



class demo:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


if __name__ == '__main__':
    date2 = demo("2021", "5", "21")
    print(sys.getsizeof(date2))
    date1 = slotsdemo("2020","4","22")
    print(sys.getsizeof(date1))

