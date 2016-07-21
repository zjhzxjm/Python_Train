# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:1.0
Introduce list data type
"""


def main():
    list_1 = [1, 2, 3]  # 创建列表 顺序存储结构 可变序列
    print list_1[0]  # 按位置索引 输出1
    list_1[0] = 'realbio'
    print list_1  # 列表为可变对象 输出['realbio', 2, 3]
    print len(list_1)  # 列表元素个数 输出3
    print list_1[:-1]  # 切片操作 list[start:end:step] 输出['realbio', 2]
    print list_1 + [4, 5]  # 列表拼接 输出['realbio', 2, 3, 4, 5]


def slice_list():
    list_1 = [1, 2, 3, 4, 5, 6]
    print list_1[0:3]  # 包括list_1[0],不包括list_1[3] 输出[1, 2, 3]
    print list_1[0:6:2]  # 步长为2 输出[1, 3, 5]
    print list_1[:-2]  # 不包括最后2个 输出[1, 2, 3, 4]
    print list_1[-2:]  # 抽取最后2个 输出[5, 6]


def sort_list():
    list_1 = [3, 6, 1, 9, 4, 11, 21]
    list_1.sort()  # 升序
    for i in list_1:
        print i
    list_1.reverse()  # 降序
    for j in list_1:
        print j


def multi_list():
    list_m = [[1, 2, 3],
              ['a', 'b', 'c'],
              ['A', 'B', 'C']]
    print list_m[0]
    print list_m[2]
    print list_m[0][2]


def compre_list():
    list_m = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    col2 = [row[1] for row in list_m]
    print col2  # 提取第二列元素并创建列表
    col3 = [row[1]+1 for row in list_m]
    print col3  # 第二列元素运算后创建列表
    colfilter = [row[1] for row in list_m if row[1]%2==0]
    print colfilter  # 第二列元素筛选出偶数后创建列表

if __name__ == "__main__":
    # main()
    # slice_list()
    # sort_list()
    multi_list()
    # compre_list()
