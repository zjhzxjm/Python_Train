# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:1.0
Introduce set data type
"""


def main():
    list_1 = [1, 2, 2, 3]
    set_1 = set(list_1)
    print set_1  # 集合为无序，不重复的元素集 输出set([1, 2, 3])
    set_2 = {2, 4, 6}
    print set_1 & set_2  # 求交运算 输出set([2])
    print set_1 - set_2  # 差运算 set_1独有元素 输出set([1, 3])
    print set_1 | set_2  # 求并运算 输出set([1, 2, 3, 4, 6])
    print set_1 ^ set_2  # 求补运算 输出set([1, 3, 4, 6])

if __name__ == '__main__':
    main()
