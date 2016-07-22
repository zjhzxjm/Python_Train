# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:1.0
Introduce operator
"""


def math_operate():
    a = 3.2
    b = 1.4
    x = a ** b
    print x  # 求幂 输出5.09577178308
    y = a / b
    print y  # 除法 输出2.28571428571
    y1 = 7 // 3
    print y1  # 整除 输出2
    y2 = 7 % 3
    print y2  # 取余 输出1


def assign_operate():
    print 1 and 0  # 输出0
    print '' and 'a'  # 输出
    print 1 or 0  # 输出1
    print '' or 'a'  # 输出a


def compare_operate():
    a = 1
    b = 1
    print a is b  # 一切数据皆对象 检验两个对象在内存中是否指向同一个对象
    print u'正数' if a > 0 else u'负数'  # 三元运算 输出“正数”

if __name__ == '__main__':
    # math_operate()
    # assign_operate()
    compare_operate()
