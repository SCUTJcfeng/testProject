# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: testProject
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-05-31 12:40:07
Last Modified: 2019-05-31 13:20:58
'''

import pytest
from main import add, minus, multi


class TestMathPytest:
    def test_add(self):
        assert 5 == add([1, 4])

    def test_minus(self):
        assert -1 == minus(1, 2)

    def test_multi(self):
        assert 0 == multi(0, 2)
        assert 2 == multi(1, 2)

    @pytest.mark.skip('skip multi')
    def test_multi_2(self):
        assert 2 == multi(1, 2)

    def test_multi_3(self):
        pytest.skip('skip multi')
        assert 2 == multi(1, 2)
