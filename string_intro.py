# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:

"""


def main():
    seq = "ATCGGTA"  # 字符串创建 不可变对象
    print str(1.0e5)  # 数值型转字符串型 输出100000.0
    print 'Realbio\tShanghai, \nRealgene, \nRealmed.'  # 转义符\
    print 'RealBio' + ' group'  # 字符串连接 + 输出RealBio group
    print 'RealBio ' * 4  # 字符串重复 * 输出RealBio RealBio RealBio RealBio
    print seq[0]  # 字符索引 输出A
    print seq[-2::-1]  # 负数步长为反序切片操作 输出TGGCTA
    print len(seq)  # 字符串长度 输出7
    tools = 'blast,blat,soap,bwa'
    list_tool = tools.split(',')
    print list_tool  # 分割字符串 输出['blast', 'blat', 'soap', 'bwa']
    print ';'.join(list_tool)  # 合并成字符串 输出blast;blat;soap;bwa
    print '..strip example..'.strip('.')  # 首尾去除指定字符 lstrip() rstrip()


def play_seqs():
    seq = '''ACCGTGCGTGACTGATACGT
    ACGTAGCTAGCGGTACCCGT'''
    print len(seq)  # 包含空格和换行符 输出45
    print seq.startswith('ACCG')  # 输出True
    print seq.endswith('CCGT')  # 输出True
    print seq.find('ACGT')  # 正向查找 输出16
    print seq.rfind('ACGT')  # 反向查找 输出25
    print seq.count('A')  # 统计匹配数 输出8
    print seq.lower()  # 将碱基统一变小写 upper（）为大写方法
    print seq.replace('ACGT', 'NNNN')  # 替换操作
    print seq.replace('ACGT', 'NNNN', 1)  # 替换操作 只替换1次


# 以下为中级课程内容
def format_string():
    print '%s %s' % ('old', 'style')  # 老的字符串格式化操作方式 输出old style
    print '{0} {1}'.format('new', 'style')  # 推荐使用 2.6及以上支持 输出new style
    print '{n:<10d} {f:>10f} {s:!^10s}'.format(f=3.2, n=4, s='realbio')  # 输出4            3.200000 !realbio!!


import re  # 需要有一定的正则表达式基础
def re_string():
    print re.match(r'Real', 'Realbio Shanghai')  # 字符串头部匹配 存在则返回对象
    print re.search(r'bio', 'Realbio Shanghai')  # 搜索字符串 存在返回对象
    print re.findall(r'h', 'Realbio Shanghai')  # 搜索字符串 返回列表 输出['h', 'h']
    seq = 'ACTTGAGTAGGCTAGC'
    print re.findall(r'ACT|AGT', seq)  # a|b a或b 输出['ACT', 'AGT']
    print re.findall(r'A[CG]T', seq)  # [ab] a 或 b 输出['ACT', 'AGT']
    print re.findall(r'A(?=G)', seq)  # 后缀 输出['A', 'A', 'A']
    print re.findall(r'(?<=G)T', seq)  # 前缀 输出['T']
    m = re.search(r'^ACTT(?P<SEQ>[ATGC]*)TAGC$', seq)  # (?P<name>expr)
    print m.group('SEQ')  # 捕获搜索结果 输出GAGTAGGC

if __name__ == '__main__':
    # main()
    # play_seqs()
    # format_string()
    re_string()
