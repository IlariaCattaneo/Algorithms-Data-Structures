from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))
from session_5 import *

def two_sum_n2(A, t):
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] + A[j] == t:
                return True
    return False

class LargestSubarraySum(unittest.TestCase):
    def test_closest_pair(self):
        A = [1, 7, 5, 3, 32, 9]
        B = [2, 3, 4, 5, 6, 7]
        n = 15
        self.assertEqual(closest_pair(A, B, n), (9, 6))

    def test_closest_pair_2(self):
        A = [1, 7, 5, 3, 32, 9]
        B = [2, 3, 4, 5, 6, 7]
        n = 25
        self.assertTrue( closest_pair(A, B, n) in [(9, 7), (32, 2)] )
        
    def test_closest_pair_3(self):
        A = [1, 1, 1, 1, 1]
        B = [2, 2, 2, 2, 2]
        n = 5
        self.assertEqual(closest_pair(A, B, n), (1, 2))

    def test_closest_pair_4(self):
        A = [1, 10, 100, 1000, 10000]
        B = [2, 3, 4, 5, 6]
        n = 10000
        self.assertEqual(closest_pair(A, B, n), (10000, 2))

    def test_basic(self):
        A = [1,-4, 2, 1, -2]
        self.assertEqual(largest_subarray_sum(A), 3)
        
    def test_ones(self):  
        A = [1, 1, 1, 1, 1]
        self.assertEqual(largest_subarray_sum(A), 5)
        
    def test_negative(self):      
        A = [-6, -7, -3, -2]
        self.assertEqual(largest_subarray_sum(A), 0)
        
    def test_jump(self):      
        A = [1, 2, 3, 4, -9, 95]
        self.assertEqual(largest_subarray_sum(A), 96)
        
    def test_empty(self):  
        A = []
        self.assertEqual(largest_subarray_sum(A), 0)
        
    def test_zero(self):      
        A = [8, 2, 4, 9, 0]
        self.assertEqual(largest_subarray_sum(A), 23)
    
    def tests_merge_intervals(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        self.assertEqual(merge_intervals(intervals), [[1,6],[8,10],[15,18]])

    def tests_merge_intervals_2(self):
        intervals = [[1,4],[4,5]]
        self.assertEqual(merge_intervals(intervals), [[1,5]])

    def tests_merge_intervals_3(self):
        intervals = [[1,4],[0,4]]
        self.assertEqual(merge_intervals(intervals), [[0,4]])

    def tests_merge_intervals_4(self):
        intervals = [[1,4],[2,3]]
        self.assertEqual(merge_intervals(intervals), [[1,4]])

    def tests_merge_intervals_5(self):
        intervals = [[1,4],[0,0]]
        self.assertEqual(merge_intervals(intervals), [[0,0],[1,4]])
    
    def tests_two_sum(self):
        A = [-3, 1]
        t = -2
        self.assertEqual(two_sum(A, t), True)

    def tests_two_sum_2(self):
        A = [-5, -4, -4, -3, -1, 2, 2, 3, 4, 6, 8]
        t = 12
        self.assertEqual(two_sum(A, t), True)

    def tests_two_sum_3(self):
        A = [-3, -1, 4, 9, 10]
        t = 1
        self.assertEqual(two_sum(A, t), True)

    def tests_two_sum_4(self):
        A = [-5, -5, -4, -1, 6, 7, 8]
        t = 12
        self.assertEqual(two_sum(A, t), False)

    def tests_two_sum_5(self):
        A = []
        t = 20
        self.assertEqual(two_sum(A, t), False)

    def tests_two_sum_6(self):
        A = [-4, -2, -2, 2, 8, 8]
        t = 15
        self.assertEqual(two_sum(A, t), False)

    def tests_two_sum_7(self):
        A = [-4, -3, -3, -1, 0, 0, 0, 4, 6, 6, 8, 9]
        t = 4
        self.assertEqual(two_sum(A, t), True)

    def test_comparison_on_on2(self):
        import random
        n = 200
        for _ in range(n):
            l = random.randint(0, 15)
            A = [random.randint(-5, 10) for _ in range(l)]
            A.sort()
            t = random.randint(-10, 25)
            assert two_sum(A, t) == two_sum_n2(A, t)
        
if __name__ == '__main__':
    unittest.main()
        