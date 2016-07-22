# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:

"""

if __name__ == "__main__":
    seq = '''>seq_name comment
ACCGTGCGTGACTGATACGT
ACGTAGCTAGCGGTACCCGT'''
    with open('test.fa', 'w') as f_out:  # with as 可自动关闭文件
        f_out.write(seq)  # 写文件
    with open('test.fa') as f_in:
        print f_in.read()  # 一次性读取文件
    with open('test.fa') as f_in:
        print f_in.readline()  # 只读取一行
    with open('test.fa') as f_in:
        lines = f_in.readlines()
        print lines  # 按行读取 返回列表
        for i in lines:
            print i.strip()

