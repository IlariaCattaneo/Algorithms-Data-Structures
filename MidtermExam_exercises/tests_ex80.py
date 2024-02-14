import unittest
from ex80 import *

class TestEx80(unittest.TestCase):
    def test_1(self):
        self.assertEqual(partition([1,2,3,4,5], 3), [1,2,3,4,5])

    def test_2(self):
        A = partition([10,2,35,4,51], 4)
        self.assertLessEqual(A[0], 4)
        self.assertLessEqual(A[1], 4)

    def test_3(self):
        A = partition([4,2,3,4,4], 4)
        self.assertGreaterEqual(A[0], 2)
        self.assertGreaterEqual(A[1], 3)
        self.assertGreaterEqual(A[2], 4)

if __name__ == '__main__':
    unittest.main()