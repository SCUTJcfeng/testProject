# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: testProject
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-05-31 09:55:00
Last Modified: 2019-05-31 11:16:01
'''

from functools import reduce


def add(*args):
    assert isinstance(args, list)
    sum_ = reduce(lambda x, y: x + y, args)
    return sum_
