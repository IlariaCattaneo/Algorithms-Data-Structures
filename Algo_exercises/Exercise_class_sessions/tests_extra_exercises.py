import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))
from extra_exercises import fibonacci, factorial, determinant, unique_characters, compress_string

class TestExercises(unittest.TestCase):
    def test_compress_string(self):
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(compress_string("aabbcc"), "aabbcc")
        self.assertEqual(compress_string("aa"), "aa")
        self.assertEqual(compress_string("a"), "a")
        self.assertEqual(compress_string("abc"), "abc")
        self.assertEqual(compress_string("aabbccaa"), "aabbccaa")
        self.assertEqual(compress_string("aabbccaaa"), "a2b2c2a3")
        self.assertEqual(compress_string("aabbccaaaa"), "a2b2c2a4")
        self.assertEqual(compress_string("aabbccaaaaa"), "a2b2c2a5")
        self.assertEqual(compress_string("aabbccaaaaaa"), "a2b2c2a6")
        self.assertEqual(compress_string("aabbccaaaaaaa"), "a2b2c2a7")
        self.assertEqual(compress_string("aabbccaaaaaaaa"), "a2b2c2a8")
        self.assertEqual(compress_string("aabbccaaaaaaaaa"), "a2b2c2a9")
        self.assertEqual(compress_string("aabbccaaaaaaaaaa"), "a2b2c2a10")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaa"), "a2b2c2a11")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaa"), "a2b2c2a12")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaa"), "a2b2c2a13")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaa"), "a2b2c2a14")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaa"), "a2b2c2a15")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaa"), "a2b2c2a16")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaaa"), "a2b2c2a17")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaaaa"), "a2b2c2a18")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaaaaa"), "a2b2c2a19")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaaaaaa"), "a2b2c2a20")

    def test_compress_string_empty(self):
        self.assertEqual(compress_string(""), "")
    
    def test_compress_string_single(self):
        self.assertEqual(compress_string("a"), "a")
        self.assertEqual(compress_string("b"), "b")
        self.assertEqual(compress_string("c"), "c")
        self.assertEqual(compress_string("d"), "d")
        self.assertEqual(compress_string("e"), "e")
    
    def test_compress_string_double(self):
        self.assertEqual(compress_string("aa"), "aa")
        self.assertEqual(compress_string("bb"), "bb")
        self.assertEqual(compress_string("cc"), "cc")
        self.assertEqual(compress_string("dd"), "dd")
        self.assertEqual(compress_string("ee"), "ee")

    def test_compress_string_triple(self):
        self.assertEqual(compress_string("aaa"), "a3")
        self.assertEqual(compress_string("bbb"), "b3")
        self.assertEqual(compress_string("ccc"), "c3")
        self.assertEqual(compress_string("ddd"), "d3")
        self.assertEqual(compress_string("eee"), "e3")
    
    def test_compress_string_quadruple(self):
        self.assertEqual(compress_string("aaaa"), "a4")
        self.assertEqual(compress_string("bbbb"), "b4")
        self.assertEqual(compress_string("cccc"), "c4")
        self.assertEqual(compress_string("dddd"), "d4")
        self.assertEqual(compress_string("eeee"), "e4")

    def test_compress_string_quintuple(self):
        self.assertEqual(compress_string("aaaaa"), "a5")
        self.assertEqual(compress_string("bbbbb"), "b5")
        self.assertEqual(compress_string("ccccc"), "c5")
        self.assertEqual(compress_string("ddddd"), "d5")
        self.assertEqual(compress_string("eeeee"), "e5")

    def test_compress_string_unique(self):
        self.assertEqual(compress_string("abcde"), "abcde")
        self.assertEqual(compress_string("fghij"), "fghij")
        self.assertEqual(compress_string("klmno"), "klmno")
        self.assertEqual(compress_string("pqrst"), "pqrst")
        self.assertEqual(compress_string("uvwxy"), "uvwxy")
        
class TestExercises(unittest.TestCase):
    # only 2x2 matrices
    def test_determinant(self):
        A = [[1, 2], [3, 4]]
        self.assertEqual(determinant(A), -2)
        A = [[1, 2], [4, 5]]
        self.assertEqual(determinant(A), -3)
        A = [[1, 2], [5, 6]]
        self.assertEqual(determinant(A), -4)
        A = [[1, 2], [6, 7]]
        self.assertEqual(determinant(A), -5)
        A = [[1, 2], [7, 8]]
        self.assertEqual(determinant(A), -6)
        A = [[1, 2], [8, 9]]
        self.assertEqual(determinant(A), -7)
    
    def test_determinant_negatives(self):
        A = [[-1, -2], [-3, -4]]
        self.assertEqual(determinant(A), -2)
        A = [[-1, -2], [-4, -5]]
        self.assertEqual(determinant(A), -3)
        A = [[-1, -2], [-5, -6]]
        self.assertEqual(determinant(A), -4)
        A = [[-1, -2], [-6, -7]]
        self.assertEqual(determinant(A), -5)
        A = [[-1, -2], [-7, -8]]
        self.assertEqual(determinant(A), -6)
        A = [[-1, -2], [-8, -9]]
        self.assertEqual(determinant(A), -7)
    
    def test_determinant_zeros(self):
        A = [[0, 0], [0, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 0], [0, 1]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 0], [1, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 0], [1, 1]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 1], [0, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 1], [0, 1]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 1], [1, 0]]
        self.assertEqual(determinant(A), -1)
        A = [[0, 1], [1, 1]]
        self.assertEqual(determinant(A), -1)
        A = [[1, 0], [0, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[1, 0], [0, 1]]
        self.assertEqual(determinant(A), 1)
        A = [[1, 0], [1, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[1, 0], [1, 1]]
        self.assertEqual(determinant(A), 1)
        A = [[1, 1], [0, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[1, 1], [0, 1]]
        self.assertEqual(determinant(A), 1)
        A = [[1, 1], [1, 0]]
        self.assertEqual(determinant(A), -1)
        A = [[1, 1], [1, 1]]
        self.assertEqual(determinant(A), 0)

class TestExercises(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(11), 39916800)
        self.assertEqual(factorial(12), 479001600)
        self.assertEqual(factorial(13), 6227020800)
        self.assertEqual(factorial(14), 87178291200)
        self.assertEqual(factorial(15), 1307674368000)
        self.assertEqual(factorial(16), 20922789888000)
        self.assertEqual(factorial(17), 355687428096000)
        self.assertEqual(factorial(18), 6402373705728000)
        self.assertEqual(factorial(19), 121645100408832000)
        self.assertEqual(factorial(20), 2432902008176640000)
        self.assertEqual(factorial(21), 51090942171709440000)
        self.assertEqual(factorial(22), 1124000727777607680000)
        self.assertEqual(factorial(23), 25852016738884976640000)

class TestExercises(unittest.TestCase):
    def test_fibonacci(self):
        # self.assertEqual(fibonacci(0), None)
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(3), [0, 1, 1])
        self.assertEqual(fibonacci(4), [0, 1, 1, 2])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(6), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fibonacci(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibonacci(11), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(fibonacci(12), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(fibonacci(13), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
        self.assertEqual(fibonacci(14), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233])
        self.assertEqual(fibonacci(15), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])

class TestExercises(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique_characters("unique"), False)
        self.assertEqual(unique_characters("uniq"), True)
        self.assertEqual(unique_characters("un"), True)
        self.assertEqual(unique_characters("u"), True)
        self.assertEqual(unique_characters(""), True)
        self.assertEqual(unique_characters("hello"), False)
        self.assertEqual(unique_characters("world"), True)
        self.assertEqual(unique_characters("python"), True)
        self.assertEqual(unique_characters("java"), False)
        self.assertEqual(unique_characters("javascript"), False)
        self.assertEqual(unique_characters("ruby"), True)
        self.assertEqual(unique_characters("perl"), True)
        self.assertEqual(unique_characters("php"), False)
        self.assertEqual(unique_characters("c"), True)
        self.assertEqual(unique_characters("c++"), False)


if __name__ == '__main__':
    unittest.main()