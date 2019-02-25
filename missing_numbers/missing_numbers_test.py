import unittest
from missing_numbers import missingNumbers

class missingNumbersTest(unittest.TestCase):
    def test_test1(self):
        self.assertEqual(missingNumbers([1,2,4,5,6]), [3])
    def test_test2(self):
        self.assertEqual(missingNumbers([1,4]), [2,3])
    def test_test3(self):
        self.assertEqual(missingNumbers([1,6]), [2,3,4,5])
if __name__ == '__main__':
    unittest.main()
