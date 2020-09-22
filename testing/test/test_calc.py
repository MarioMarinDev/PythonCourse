import unittest
from calc import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-10, 5), -5)
        self.assertEqual(calc.add(10, -5), 5)
        self.assertEqual(calc.add(5, 0), 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-10, 5), -15)
        self.assertEqual(calc.subtract(10, -5), 15)
        self.assertEqual(calc.subtract(5, 0), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-10, 5), -50)
        self.assertEqual(calc.multiply(10, -5), -50)
        self.assertEqual(calc.multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-10, 5), -2)
        self.assertEqual(calc.divide(10, -5), -2)
        self.assertRaises(ValueError, calc.divide, 5, 0)
        with self.assertRaises(ValueError):
            calc.divide(5, 0)

    def test_calculate(self):
        self.assertEqual(calc.calculate("5 + 5"), 10)
        self.assertEqual(calc.calculate("10 - 50"), -40)
        self.assertEqual(calc.calculate("5 * 5"), 25)
        self.assertEqual(calc.calculate("50 / 5"), 10)
        self.assertRaises(ValueError, calc.calculate, "5 / 0")
        with self.assertRaises(ValueError):
            calc.calculate("5 +")
        with self.assertRaises(ValueError):
            calc.calculate("5 + 5 - 10")
        with self.assertRaises(ValueError):
            calc.calculate("a + 5")
        with self.assertRaises(ValueError):
            calc.calculate("10 ! 5")


if __name__ == '__main__':
    unittest.main()
