#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/27 12:37
# @Author : Crolmo
# @Site : 
# @File : io_operating.py
# @Software: PyCharm
import os


def print_to_file():
    with open("test",'wt') as f:
        print("test",file=f)


def sep_test():
    print("1","2","3",sep="/")


def end_test():
    for i in range(10):
        print(i,end=",")


def file_not_exists_to_write():
    with open('test','xt') as f:
        print("crolmo",file=f)



if __name__ == '__main__':
    print_to_file()
    sep_test()
    end_test()
    file_not_exists_to_write()