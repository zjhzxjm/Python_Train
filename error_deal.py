# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:

"""


def error_deal():
    list_1 = [1, 2, 3]
    while True:
        value = input('Position [0 to quit]?')
        if value == 0:
            break
        try:
            position = int(value)
            print(list_1[position])
        except IndexError:
            print u"该位置不存在值：", position
        except Exception as err:
            print u"错误信息：", err

if __name__ == "__main__":
    error_deal()
