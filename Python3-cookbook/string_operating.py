#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/25 18:29
# @Author : Crolmo
# @Site : 
# @File : string_operating.py
# @Software: PyCharm

import re
import textwrap
import unicodedata

def check_string_start_and_end():
    url = "http://www.baidu.com"
    print(url.startswith("http"))
    print(url.endswith(".com"))


def string_re():
    string_A = "Process finished with exit code 0"
    string_B = string_A.replace("0", "1")
    print(string_B)
    datepat = re.compile(r"exit")
    data1 = datepat.match(string_A)
    print(data1)

    data2 = datepat.findall(string_A)
    print(data2)

    data3 = re.sub(r"exit",r"test", string_A)
    print(data3)


def unicode_standardization():
    data = "Spicy Jalape\u00f1o"
    print(unicodedata.normalize("NFC",data))


def delete_string():
    data = "------Spicy Jalapeño leons===== \n"
    print(data.strip())
    print(data.lstrip('-'))
    print(data.strip('= \n'))


def replace_string():
    data = "------Spicy Jalapeño leons===== \n"
    print(data.replace('-','?'))


def align_string():
    data = "test align sting"
    print(data.ljust(30))
    print(data.rjust(30))
    print(data.ljust(30,"-"))
    print(format(data,'>30'))
    print(format(data,'<30'))
    print('{:>10s} {:>10s}'.format('Hello', 'World'))


def merge_string():
    '''
    每一次执行+=操作的时候会创建一个新的字符串对象,消耗内存
    构建大量小字符串的输出代码， 最好考虑使用生成器函数
    '''
    data = ["A","B","C","D"]
    print(" ".join(data))
    print("A" + " " + "B")

    def sample():
        yield 'Is'
        yield 'Chicago'
        yield 'Not'
        yield 'Chicago?'

    strC = " ".join(sample())
    print(strC)


def format_string_print():
    data = "(web-venv) D:\GitProject\Crols-Test-Platform\Python3-cookbook>D:/GitProject/Crols-Test-Platform/Python3-cookbook/string_operating.py"
    print(textwrap.fill(data,70,initial_indent='    '))


if __name__ == '__main__':
    check_string_start_and_end()
    string_re()
    unicode_standardization()
    delete_string()
    replace_string()
    align_string()
    merge_string()
    format_string_print()