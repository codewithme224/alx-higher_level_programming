#!/usr/bin/python3
"""Test for the square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_attributes(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        s = Square(10, 2, 3, 4)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_str(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update(self):
        s = Square(5, 1, 2, 3)
        s.update(4, 10, 20, 30)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)

        s.update(y=50, size=15, id=5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 50)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 3)
        d = s.to_dictionary()
        self.assertDictEqual(d, {'id': 3, 'size': 5, 'x': 1, 'y': 2})


if __name__ == "__main__":
    unittest.main()
