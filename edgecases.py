import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)

def divide(a, b):
    return a / b

class TestUnexpected(unittest.TestCase):
    def test_get_sqrt_good(self):
        self.assertEqual(get_sqrt(144), 12)

    def test_get_sqrt_negative(self):
        with self.assertRaises(ValueError):
            get_sqrt(-100)

    def test_divide_good(self):
        # Fixed: included both arguments
        self.assertEqual(divide(144, 12), 12)

    def test_divide_zero(self):
        # Testing division by zero
        with self.assertRaises(ZeroDivisionError):
            divide(100, 0)

if __name__ == '__main__':
    unittest.main()
