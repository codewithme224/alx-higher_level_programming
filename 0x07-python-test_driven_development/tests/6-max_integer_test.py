#!/usr/bin/python3
"""  
testing for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

""" A testcase is created by subclassing unittest.TestCase"""
class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_only_one(self):
        """Test list with only one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple(self):
        """Test list with multiple elements"""
        self.assertEqual(max_integer([1, 2, 10, 5, 8]), 10)

    def test_negative(self):
        """Test list with negative elements"""
        self.assertEqual(max_integer([-1, -5, -3, -9]), -1)

    def test_repeated(self):
        """ Test list with repeated elements """
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

if __name__ == '__main__':
    unittest.main()
