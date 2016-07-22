# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:

"""


def func_arguments(required1, a='1', b='2'):
    print u"位置参数required1:", required1  # 定义函数时位置参数要放在最前面
    print u"关键字参数a：", a, "b:", b


def gather_arguments(*args, **kwargs):
    print u"捕获所有位置参数：", args
    print u"捕获所有关键词参数：", kwargs


def outer(out_str):
    def inner(in_str):
        return "inner func result: %s + %s" % (out_str, in_str)
    return inner  # 返回闭包（一个含有环境变量取值的函数对象）


def edit_words(words, func):
    for word in words:
        print func(word)


def cap_func(word):
    return word.capitalize() + '!'

if __name__ == "__main__":
    # func_arguments(0)  # 位置参数为必须参数，而关键词参数已定义默认值非必须
    # func_arguments(0, b=3, a=5)  # 关键词参数无需关注顺序
    # gather_arguments(1, 2, a=3, b=4)  # 位置参数捕获后返回元组，关键词参数捕获后返回字典
    # inner_a = outer('A')
    # inner_b = outer('B')
    # print inner_a  # 闭包 <function inner at 0x0000000002CE2048>
    # print inner_b  # 闭包 <function inner at 0x0000000002D520B8>
    # print inner_a('a')  # 输出inner func result: A + a
    # print inner_b('b')  # 输出inner func result: B + b
    words = ['realbio', 'realgene', 'realmed']
    edit_words(words, cap_func)
    edit_words(words, lambda word: word.capitalize() + '!')