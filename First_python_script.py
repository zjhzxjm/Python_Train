# -*- coding: utf-8 -*-
"""
Author: xujm@realbio.cn
Ver:1.0
My first app
"""

import sys


def app(name):
    print name + "'s first app"
# 第一个Python程序
if __name__ == "__main__":
    my_name = sys.argv[1]
    app(my_name)
