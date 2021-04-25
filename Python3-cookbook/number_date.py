#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/25 20:04
# @Author : Crolmo
# @Site : 
# @File : number_date.py
# @Software: PyCharm

import cmath
import random
from decimal import Decimal
from datetime import timedelta
from datetime import datetime

def round_number():
    print(round(1.35, 1))
    print(round(Decimal(1.35),1))
    print(format(1.35,'0.1f'))


def base_conversion():
    x = 123
    print(bin(x),format(x,'b'))
    print(oct(x),format(x,'o'))
    print(hex(x),format(x,'x'))


def complex_number_operations():
    a = complex(1,3)
    print(a,"实部：{}，虚部：{},共轭复数: {}".format(a.real,a.imag,a.conjugate()))
    print("余弦值：{}，正弦值：{}，平方根：{}".format(cmath.cos(a),cmath.sin(a),cmath.exp(a)))


def random_number():
    nums = list(range(10))
    print(random.choice(nums))
    print(random.sample(nums,3))
    random.shuffle(nums)
    print(nums)
    print(random.randint(0,100))
    print(random.random())
    print(random.getrandbits(30))


def date_operations():
    date_delta = timedelta(days=2,hours=2,minutes=3,seconds=3)
    print(date_delta,date_delta.total_seconds())
    date_time = datetime(2021,4,25)
    print(date_time)
    date1 = "2021-09-22"
    print(datetime.strptime(date1, '%Y-%m-%d'))


if __name__ == '__main__':
    round_number()
    base_conversion()
    complex_number_operations()
    random_number()
    date_operations()