#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/25 20:53
# @Author : Crolmo
# @Site : 
# @File : Generators_iterators.py
# @Software: PyCharm
import heapq
from itertools import chain
from itertools import islice
from itertools import dropwhile
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

def enumerate_test():
    my_list = ['a', 'b', 'c']
    for index,value in enumerate(my_list):
        print(index,value)


def dropwhile_test():
    pass
    dropwhile("","")


def islice_test():
    items = ['a', 'b', 'c', 1, 4, 10, 15]
    for x in islice(items, 3, None):
        print(x)
    for y in islice(items, None, 3):
        print(y)


def sort_item():
    items = ['a', 'b', 'c']
    for p in permutations(items,1):
        print(p)
    for c in combinations(items, 2):
        print(c)
    for c in combinations_with_replacement(items, 3):
        print(c)


def zip_test():
    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]
    for i in zip(headers,values):
        print(i)


def chain_test():
    a = [1, 2, 3]
    b = [4, 6, 5]
    for i in chain(a,b):
        print(i)


def marge_item():
    a = [1,2,3]
    b = [4,6,5]
    for c in heapq.merge(a, b):
        print(c)


def iter_test():
    a = 0
    for i in iter(lambda : a,10):
        a += 1
        print(i)


if __name__ == '__main__':
    enumerate_test()
    dropwhile_test()
    islice_test()
    sort_item()
    zip_test()
    chain_test()
    marge_item()
    iter_test()