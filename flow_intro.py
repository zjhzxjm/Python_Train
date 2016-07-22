# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:1.0
Introduce flow
"""


def condition_flow():
    score = 80
    if 60 <= score < 100:  # 多重比较
        if score > 90:
            print u"优秀"
        elif score > 80:
            print u"良好"
        else:
            print u"合格"
    else:
        print u"不合格"  # 嵌套使用


def repeat_while1_flow():
    while True:
        value = input("Integer, please [0 to quit]")
        if value == 0:
            break  # 退出循环
        number = int(value)
        if number % 2 == 0:
            continue  # 不再执行剩余代码，直接进入下一个循环
        print u"您输入了非偶数：", number


def repeat_while2_flow():
    numbers = [1, 3, 5]
    position = 0
    while position < len(numbers):
        number = numbers[position]
        if number % 2 == 0:
            print u"偶数", number
            break
        position += 1
    else:  # break未执行情况下执行该代码块
        print u"未找到偶数"


def repeat_for_flow():
    numbers = [1, 2, 3]
    for i in numbers:
        print i  # 相比用上述while方式更Pythonic
    seq = 'ATCGA'
    for base in seq:
        print base  # 可以对字符串进行循环操作 输出各字符
    dict_1 = {"a": 1, "b": 2}
    for i in dict_1:
        print i  # 与dict_1.keys()相同 输出各键
    for item in dict_1.items():
        print item  # 输出各键值对的元组
    for k, v in dict_1.items():
        print k, v  # 运用元组解包方法
# break continue else同样适用于for循环

if __name__ == "__main__":
    # condition_flow()
    # repeat_while1_flow()
    # repeat_while2_flow()
    repeat_for_flow()
