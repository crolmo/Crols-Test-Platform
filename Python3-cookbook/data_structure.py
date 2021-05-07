#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/25 15:46
# @Author : Crolmo
# @Site : 
# @File : data_structure.py
# @Software: PyCharm

import heapq
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
from operator import itemgetter
from itertools import groupby
from itertools import compress


def iter_to_obj(*args):
    '''
    任何的序列（或者是可迭代对象）可以通过一个简单的赋值操作来分解为单独的变量。 唯一的要求就是变量的总数和结构必须与序列相吻合
    '''
    count = len(args)
    for obj in range(count):
        print(args[obj])
    try:
        a,b,c,d = args
    except ValueError as e:
        return e


def multiple_to_obj(*args):
    '''
    多个不确定的变量赋值
    '''
    first, *medium, last = args
    print("first object is {}".format(first))
    print("medium object is {}".format(medium))
    print("last object is {}".format(last))


def max_min_element(*args):
    max = heapq.nlargest(1,args)
    min = heapq.nsmallest(1,args)
    print("max element is {},min element is {}".format(max,min))


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def priorityqueue():
    q = PriorityQueue()
    q.push("A",1)
    q.push("B",5)
    q.push("C",2)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    try:
        print(q.pop())
    except IndexError as e:
        return e


def multiple_dict():
    d1 = defaultdict(list)
    d1["a"].append(1)
    d1["b"].append(2)
    print(d1)

    d2 = {}
    d2.setdefault('a',[]).append(2)
    d2.setdefault('a',[]).append(3)
    print(d2)

    d3 = defaultdict(set)
    d3["a"].add(1)
    d3["b"].add(2)
    print(d3)


def order_dict():
    d = OrderedDict()
    d['foo1'] = 1
    d['bar2'] = 2
    d['spam3'] = 3
    d['grok4'] = 4
    for key in d:
        print(key)


def sorted_dict_by_value():
    d = {"A": 1,
         "B": 2,
         "C": 3
         }
    result = sorted(zip(d.values(),d.keys()))
    print(result)


def slice_style():
    items = [0, 1, 2, 3, 4, 5, 6]
    midslice = slice(2,5,2)
    print(items[midslice])


def mostobj():
    '''
    序列中出现次数最多的元素
    '''
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    word_count = Counter(words)
    top_three = word_count.most_common(3)
    print(top_three)

def sort_by_anykey():
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_fname)
    print(rows_by_uid)

def group_by_anykey():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    rows.sort(key=itemgetter('date'))
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)


def filter_by_boolean():
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    lboolean = [False,True,False,True,False,True,False,True]
    fdata = compress(addresses,lboolean)
    print(list(fdata))


if __name__ == '__main__':
    iter_to_obj("A","B","C")
    multiple_to_obj("A","B","C","D")
    max_min_element(1,2,3,4)
    priorityqueue()
    multiple_dict()
    order_dict()
    sorted_dict_by_value()
    slice_style()
    mostobj()
    sort_by_anykey()
    group_by_anykey()
    filter_by_boolean()
