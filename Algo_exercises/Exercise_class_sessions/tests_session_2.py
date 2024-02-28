import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))
from session_2 import check_sorted, count_lower, find_peak, leap_year, multiples_of_three, partition_even_odd

def check_partition_even_odd( A ):
    for i in range(len(A)-1):
        if A[i] % 2 == 1:
            for j in range(i+1, len(A)):
                if A[j] % 2 == 0:
                    return False
    return True

class TestExercises(unittest.TestCase):
    def test_check_sorted(self):
        self.assertEqual(check_sorted([1, 2, 3, 4, 5]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), True)
        self.assertEqual(check_sorted([34, 31, 45, 5, 38, 19, 19, 26, 25, 19, 39, 40]), False)
        self.assertEqual(check_sorted([7, 2, 0]), False)

    def test_check_sorted_empty(self):
        self.assertEqual(check_sorted([]), True)

    def test_check_sorted_negative(self):
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]), False)
        self.assertEqual(check_sorted([-34, -31, -45, -5, -38, -19, -19, -26, -25, -19, -39, -40]), False)
        self.assertEqual(check_sorted([-7, -2, 0]), True)

    def test_check_sorted_float(self):
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]), True)
        self.assertEqual(check_sorted([34.0, 31.0, 45.0, 5.0, 38.0, 19.0, 19.0, 26.0, 25.0, 19.0, 39.0, 40.0]), False)
        self.assertEqual(check_sorted([7.0, 2.0, 0.0]), False)

    def test_check_sorted_mixed(self):
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0, 11]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0, 11, 12.0]), True)
        self.assertEqual(check_sorted([34, 31.0, 45, 5.0, 38, 19, 19.0, 26, 25, 19.0, 39, 40]), False)
        self.assertEqual(check_sorted([7, 2.0, 0]), False)

    def test_count_lower(self):
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 6), 5)
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 0), 0)
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 1), 0)
    
    def test_count_lower_empty(self):
        self.assertEqual(count_lower([], 3), 0)
    
    def test_count_lower_negative(self):
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], -3), 2)
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], -6), 0)
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], 0), 5)
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], -5), 0)
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], -1), 4)

    def test_count_lower_float(self):
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 3.3), 2)
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 6.6), 5)
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 0.0), 0)
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 5.5), 4)
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 1.1), 0)

    def test_count_lower_mixed(self):
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 3), 2)
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 6), 5)
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 0), 0)
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 5), 4)
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 1), 0)

    def test_count_lower_string(self):
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], 'c'), 2)
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], 'f'), 5)
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], '0'), 0)
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], 'e'), 4)
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], 'a'), 0)
        
    def test_find_peak(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 11)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 12)
        self.assertEqual(find_peak([34, 31, 45, 5, 38, 19, 19, 26, 25, 19, 39, 40]), 45)
        self.assertEqual(find_peak([7, 2, 0]), 7)
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

    def test_leap_year(self):
        self.assertEqual(leap_year(2000), True)
        self.assertEqual(leap_year(1969), False)
        self.assertEqual(leap_year(2023), False)
        self.assertEqual(leap_year(1984), True)
        self.assertEqual(leap_year(2022), False)
        self.assertEqual(leap_year(2200), False)
        self.assertEqual(leap_year(2400), True)
        self.assertEqual(leap_year(1900), False)
        self.assertEqual(leap_year(1600), True)
        self.assertEqual(leap_year(2004), True)
        self.assertEqual(leap_year(2008), True)
    
    def test_leap_year_negative(self):
        self.assertEqual(leap_year(-2000), True)
        self.assertEqual(leap_year(-1969), False)
        self.assertEqual(leap_year(-2023), False)
        self.assertEqual(leap_year(-1984), True)
        self.assertEqual(leap_year(-2022), False)
        self.assertEqual(leap_year(-2200), False)
        self.assertEqual(leap_year(-2400), True)
        self.assertEqual(leap_year(-1900), False)
        self.assertEqual(leap_year(-1600), True)
        self.assertEqual(leap_year(-2004), True)
        self.assertEqual(leap_year(-2008), True)

    def test_leap_year_float(self):
        self.assertEqual(leap_year(2000.0), True)
        self.assertEqual(leap_year(1969.0), False)
        self.assertEqual(leap_year(2023.0), False)
        self.assertEqual(leap_year(1984.0), True)
        self.assertEqual(leap_year(2022.0), False)
        self.assertEqual(leap_year(2200.0), False)
        self.assertEqual(leap_year(2400.0), True)
        self.assertEqual(leap_year(1900.0), False)
        self.assertEqual(leap_year(1600.0), True)
        self.assertEqual(leap_year(2004.0), True)
        self.assertEqual(leap_year(2008.0), True)
    
    def test_multiples_of_three(self):
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5]), 1)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6]), 2)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6, 7, 8, 9]), 3)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 3)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 4)
        self.assertEqual(multiples_of_three([34, 31, 45, 5, 38, 19, 19, 26, 25, 19, 39, 40]), 2)
        self.assertEqual(multiples_of_three([7, 2, 0]), 1)

    def test_multiples_of_three_empty(self):
        self.assertEqual(multiples_of_three([]), 0)

    def test_multiples_of_three_negative(self):
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5]), 1)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6]), 2)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6, -7, -8, -9]), 3)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), 3)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]), 3)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]), 4)
        self.assertEqual(multiples_of_three([-34, -31, -45, -5, -38, -19, -19, -26, -25, -19, -39, -40]), 2)
        self.assertEqual(multiples_of_three([-7, -2, 0]), 1)

    def test_multiples_of_three_float(self):
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0]), 1)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]), 2)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]), 3)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]), 3)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]), 3)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]), 4)
        self.assertEqual(multiples_of_three([34.0, 31.0, 45.0, 5.0, 38.0, 19.0, 19.0, 26.0, 25.0, 19.0, 39.0, 40.0]), 2)
        self.assertEqual(multiples_of_three([7.0, 2.0, 0.0]), 1)
    
    def test_multiples_of_three_mixed(self):
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5]), 1)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0]), 2)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9]), 3)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0]), 3)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0, 11]), 3)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0, 11, 12.0]), 4)
        self.assertEqual(multiples_of_three([34, 31.0, 45, 5.0, 38, 19, 19.0, 26, 25, 19.0, 39, 40]), 2)
        self.assertEqual(multiples_of_three([7, 2.0, 0]), 1)
    
    def test_partition_even_odd(self):
        A = [1, 2, 3, 4, 5]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [1, 2, 3, 4, 5, 6]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

    def test_partition_even_odd_empty(self):
        A = []
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

    def test_partition_even_odd_negative(self):
        A = [-1, -2, -3, -4, -5]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [-1, -2, -3, -4, -5, -6]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)
    
if __name__ == '__main__':
    unittest.main()