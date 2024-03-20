from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
import timeit
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))
from session_4 import *
    
def check_partition_even_odd( A ):
    even = True
    for i in range(len(A)):
        if A[i] % 2 == 0:
            if not even:
                return False
        else:
            even = False
    return True

def algo_x(n):
    assert n >= 0
    m = 0
    while m*m <= n:
        m = m + 1
    return m - 1

class TestExercises(unittest.TestCase):
    def test_find_peak(self):
        self.assertEqual(find_peak([1, 3, 20, 4, 1, 0]),20)
        self.assertEqual(find_peak([1, 3, 20, 4, 1, 0, 1]),20)
        self.assertEqual(find_peak([1,2,3]),3)
        self.assertEqual(find_peak([1,2,7,8,9]),9)
        self.assertEqual(find_peak([9,6,5]),9)
        self.assertEqual(find_peak([1,2,1,-3]),2)
        self.assertEqual(find_peak([1,2,1,0,-3]),2)
        self.assertEqual(find_peak([1,2,3,2,1]),3)
        self.assertEqual(find_peak([1,2,3,4]),4)
        self.assertEqual(find_peak([1,2]),2)
        self.assertEqual(find_peak([4,7,4]),7)
        self.assertEqual(find_peak([7]),7)
        self.assertEqual(find_peak([7,4]),7)
        self.assertEqual(find_peak([4,7]),7)

    def tests_find_peak_flat(self):
        self.assertEqual(find_peak([0,0,0,0]),0)
        self.assertEqual(find_peak([1,1,1,1]),1)
        self.assertEqual(find_peak([2,2,2,2]),2)
        self.assertEqual(find_peak([3,3,3,3]),3)
        self.assertEqual(find_peak([4,4,4,4]),4)
        self.assertEqual(find_peak([5,5,5,5]),5)
        self.assertEqual(find_peak([6,6,6,6]),6)
        self.assertEqual(find_peak([7,7,7,7]),7)
        self.assertEqual(find_peak([8,8,8,8]),8)
        self.assertEqual(find_peak([9,9,9,9]),9)
        self.assertEqual(find_peak([10,10,10,10]),10)

    def test_better_algo_x(self):
        ns = [n for n in range(1000)]
        for n in ns:
            self.assertEqual(better_algo_x(n),algo_x(n))
    
    def test_better_algo_x_0(self):
        self.assertEqual(better_algo_x(0),algo_x(0))

    def test_performance(self):
        test_values = [10000, 100000, 1000000, 10000000, 100000000]

        for n in test_values:
            time_algo_x = timeit.timeit(lambda: algo_x(n), number=100)
            time_better_algo_x = timeit.timeit(lambda: better_algo_x(n), number=100)
            self.assertTrue(time_better_algo_x <= time_algo_x, f"better_algo_x is not faster than algo_x for n={n}")
        
    def test_lps(self):
        self.assertEqual(lps('babad'),'bab' or 'aba')
        self.assertEqual(lps('cbbd'),'bb')
        self.assertEqual(lps('a'),'a')
        self.assertEqual(lps('ac'),'a')
        self.assertEqual(lps('bb'),'bb')
        self.assertEqual(lps('ccc'),'ccc')
        self.assertEqual(lps('aaaa'),'aaaa')
        self.assertEqual(lps('racecarlevel'),'racecar')
    
    def test_md(self):
        self.assertEqual(md([2, 1, 5, 9, 4, 10, 8]),9)
        self.assertEqual(md([2, 1, 5, 9, 4, 10, 8, 6]),9)
        self.assertEqual(md([2, 1, 5, 9, 4, 10, 8, 6, 3]),9)
        self.assertEqual(md([1]),0)
        self.assertEqual(md([1, 1, 1]),0)
        self.assertEqual(md([10, -3, 4, 11, 0, 9]),14)

    def test_min(self):
        A = [1,2,3,4,5]
        self.assertEqual(min(A),1)
        A = [5,4,3,2,1]
        self.assertEqual(min(A),1)
        A = [1,2,3,4,1]
        self.assertEqual(min(A),1)
        A = [1,2,3,4,0]
        self.assertEqual(min(A),0)
        A = [1,2,3,4,5,0]
        self.assertEqual(min(A),0)
        A = [1,2,3,4,5,0,0]
        self.assertEqual(min(A),0)
        A = [1,2,3,4,5,0,0,0]
        self.assertEqual(min(A),0)

    def test_max(self):
        A = [1,2,3,4,5]
        self.assertEqual(max(A),5)
        A = [5,4,3,2,1]
        self.assertEqual(max(A),5)
        A = [1,2,3,4,1]
        self.assertEqual(max(A),4)
        A = [1,2,3,4,0]
        self.assertEqual(max(A),4)
        A = [1,2,3,4,5,0]
        self.assertEqual(max(A),5)
        A = [1,2,3,4,5,0,0]
        self.assertEqual(max(A),5)
        A = [1,2,3,4,5,0,0,0]
        self.assertEqual(max(A),5)

    def tests_palindrome(self):
        self.assertEqual(palindrome('aba'),True)
        self.assertEqual(palindrome('abba'),True)
        self.assertEqual(palindrome('abcba'),True)
        self.assertEqual(palindrome('abccba'),True)
        self.assertEqual(palindrome('racecar'),True)
        self.assertEqual(palindrome('level'),True)
        self.assertEqual(palindrome('rotator'),True)
    
    def tests_palindrome_false(self):
        self.assertEqual(palindrome('ab'),False)
        self.assertEqual(palindrome('abc'),False)
        self.assertEqual(palindrome('abca'),False)
        self.assertEqual(palindrome('abcc'),False)
        self.assertEqual(palindrome('racecar1'),False)
        self.assertEqual(palindrome('level1'),False)
        self.assertEqual(palindrome('rotator1'),False)

    def test_partition_even_odd(self):
        A = [-1,1,7,5,-2,1,2,7,7,5,5,1,1,4,1]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [1,2,3,4,5,6,7,8,9,10]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [1,1,1,1,1,1,1,1,1,1]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [2,2,2,2,2,2,2,2,2,2]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [i for i in range(100)]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [i for i in range(100,0,-1)]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [i for i in range(100,0,2)]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

    def test_prime_factorize(self):
        self.assertEqual(prime_factorize(2312).strip(), "2E3 17E2")
        self.assertEqual(prime_factorize(10242311).strip(), "19 701 769")
        self.assertEqual(prime_factorize(1).strip(), "")
        self.assertEqual(prime_factorize(2).strip(), "2")
        self.assertEqual(prime_factorize(3).strip(), "3")
        self.assertEqual(prime_factorize(4).strip(), "2E2")
        self.assertEqual(prime_factorize(5).strip(), "5")
        self.assertEqual(prime_factorize(6).strip(), "2 3")
        self.assertEqual(prime_factorize(7).strip(), "7")
        self.assertEqual(prime_factorize(8).strip(), "2E3")
        self.assertEqual(prime_factorize(9).strip(), "3E2")
        self.assertEqual(prime_factorize(10).strip(), "2 5")
        self.assertEqual(prime_factorize(11).strip(), "11")
        self.assertEqual(prime_factorize(12).strip(), "2E2 3")
        self.assertEqual(prime_factorize(13).strip(), "13")
        self.assertEqual(prime_factorize(14).strip(), "2 7")
        self.assertEqual(prime_factorize(15).strip(), "3 5")
        self.assertEqual(prime_factorize(16).strip(), "2E4")
        self.assertEqual(prime_factorize(17).strip(), "17")
        self.assertEqual(prime_factorize(18).strip(), "2 3E2")



if __name__ == '__main__':
    unittest.main()
        