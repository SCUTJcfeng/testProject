# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: testProject
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-05-31 10:13:40
Last Modified: 2019-05-31 12:12:46
'''

import unittest
from main import add, minus, multi


class TestMath(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'test class set up')

    @classmethod
    def tearDownClass(cls):
        print(f'test class tear down')

    def setUp(self):
        print(f'test method set up')

    def tearDown(self):
        print(f'test tear down')

    def test_add(self):
        self.assertEqual(4950, add([i for i in range(100)]))

    # @unittest.skip('skip test')
    def test_minus_skip(self):
        self.assertEqual(-1, minus(0, 1))

    def test_minus(self):
        self.assertEqual(0, minus(9, 9))

    def test_multi(self):
        # self.skipTest('skip test_multi')
        self.assertEqual(9, multi(1, 9))


def test_with_order():
    suite = unittest.TestSuite()
    tests = [
        TestMath('test_add'),
        TestMath('test_minus'),
        TestMath('test_multi')
    ]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def default_test():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    default_test()
    test_with_order()
