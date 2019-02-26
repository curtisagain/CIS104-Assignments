import unittest
import calculator

class Tests(unittest.TestCase):
    
    def testsAdd(self):
        self.assertEqual(calculator.add(0, -5), -5)
        self.assertEqual(calculator.add(11, 11), 22)
        self.assertEqual(calculator.add(0.1, 3), 3.1)

    def testSubtract(self):
        self.assertEqual(calculator.subtract(14, 4), 10)
        self.assertEqual(calculator.subtract(-2, 4), -6)
        self.assertEqual(calculator.subtract(0.2, 1), -0.8)

    def testMultiply(self):
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.multiply(7, -7), -49)
        self.assertEqual(calculator.multiply(0.2, 5), 1)

    def testDivide(self):
        self.assertEqual(calculator.divide(4, 2), 2)
        self.assertEqual(calculator.divide(2, -4), -0.5)
        self.assertEqual(calculator.divide(22, 2), 11)

    def testPower(self):
        self.assertEqual(calculator.pow(6, 1), 6)
        self.assertEqual(calculator.pow(2, -4), 0.0625)
        self.assertEqual(calculator.pow(22, 0.5), 4.69041575982343)

    def testInvert(self):
        self.assertEqual(calculator.invert(0), 0)
        self.assertEqual(calculator.invert(-4), 4)
        self.assertEqual(calculator.invert(-11), 11)

if __name__ ==  '__main__':
    unittest.main()