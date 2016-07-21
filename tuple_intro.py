# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:1.0
Introduce tuple data type
"""


def main():
    tuple_1 = (1, 2, 'a')  # 创建元组 比列表速度快 不可变序列 属性与列表基本一致
    print tuple_1[0]  # 输出1
    tuple_2 = (('a', 'b'), ('A', 'B'))
    print tuple_2[0][1]  # 输出b
    x, y, z = tuple_1
    print x, y, z  # 解包 输出1 2 a
    i = 1
    j = 2
    j, i = i, j  # 创建元组可以省略括号 交换数据
    print i, j

if __name__ == '__main__':
    main()