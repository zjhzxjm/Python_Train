# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:1.0
Introduce dictionary data type
"""


def main():
    dict_1 = {'a': 1, 'b': 2, 'c': 3}  # 创建字典 无需存储结构 键（key）值（value）对构成
    print dict_1['a']  # 字典索引
    dict_1['d'] = 4
    print dict_1  # 字典的添加 输出{'a': 1, 'c': 3, 'b': 2, 'd': 4}
    dict_1['d'] += 1
    print dict_1  # 字典的修改 输出{'a': 1, 'c': 3, 'b': 2, 'd': 5}
    del(dict_1['a'])
    print dict_1  # 字典的删除 输出{'c': 3, 'b': 2, 'd': 5}
    print dict_1.pop('b')  # 字典的删除并返回被删的值 输出2
    for k in dict_1:
        print k, dict_1[k]  # 字典的遍历
    print dict_1.keys()  # 获取keys的列表 输出['c', 'd']
    print dict_1.values()  # 获取values的列表 输出[3, 5]


def sort_dict():
    dict_2 = {}
    dict_2['A'] = 1
    dict_2['B'] = 2
    dict_2['C'] = 3
    print dict_2  # 另一种方法创建字典
    ks = dict_2.keys()
    ks.sort()
    print ks
    for k in ks:
        print k, '=>', dict_2[k]
    for k in sorted(dict_2):
        print k, '=>', dict_2[k]  # 通过键值进行排序

if __name__ == '__main__':
    # main()
    sort_dict()