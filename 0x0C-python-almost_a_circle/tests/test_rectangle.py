#!/usr/bin/python3
""" Test for the rectangle class """
from contextlib import redirect_stdout
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display()
            output = buffer.getvalue()
            self.assertEqual(output, expected_output)

    def test_str(self):
        r = Rectangle(5, 10, 15, 20, 25)
        self.assertEqual(str(r), "[Rectangle] (25) 15/20 - 5/10")

    def test_update(self):
        r = Rectangle(5, 10, 15, 20, 25)
        r.update(30, 20, 15, 10, 5)
        self.assertEqual(str(r), "[Rectangle] (30) 10/5 - 20/15")

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 15, 20, 25)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 25, 'width': 5, 'height': 10, 'x': 15, 'y': 20})


if __name__ == "__main__":
    unittest.main()
