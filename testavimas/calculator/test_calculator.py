import unittest
from calculator import add, substract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(4, add(2, 2))
        self.assertEqual(-4, add(-2, -2))
    
    def test_substract(self):
        self.assertEqual(10, substract(20, 10))
        self.assertEqual(40, substract(45, 5))

    def test_multiply(self):
        self.assertEqual(4, multiply(-2, -2))
        self.assertEqual(9, multiply(3, 3))

    def test_divide(self):
        self.assertEqual(1, divide(-2, -2))
        self.assertEqual(10, divide(100, 10))
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

if __name__ == '__main__':
    unittest.main()

                    
