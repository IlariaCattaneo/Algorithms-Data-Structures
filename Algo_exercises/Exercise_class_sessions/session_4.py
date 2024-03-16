def find_peak(A):
    begin = 0
    end = len(A)
    if len(A) == 0:
        return None
    elif len(A) == 1:
        return A[0]
    while begin < end:
        mid = (begin + end)//2
        if abs(begin-(end-1)) == 1 or abs(begin-(end-1)) == 0:
            if A[begin] > A[end-1]:
                return A[begin]
            else:
                return A[end-1]
        elif (A[mid - 1] <= A[mid] and A[mid] >= A[mid + 1]):
            return A[mid]
        elif A[mid] >= A[mid - 1]:
            begin = mid + 1
        elif A[mid] <= A[mid - 1]:
            end = mid
    return A[begin]


# algo_x takes an integer n and returns the closest integer to the square root of n
# worst case complexity: theta(sqrt(n))
# worst case complexity of better_algo_x: theta(log n)
def better_algo_x(n):
    assert n >= 0
    low = 0
    high = n + 1
    while low < high:
        m = (low + high) // 2
        if m*m > n:
            high = m
        elif m*m < n:
            low = m + 1
        else:
            return m
    return low - 1


def min(A):
    min = A[0]
    for number in A:
        if number < min:
            min = number
    return min


def max(A):
    max = A[0]
    for number in A:
        if number > max:
            max = number
    return max

def palindrome(s):
    begin = 0
    end = len(s) - 1
    while begin < end:
        if s[begin] == s[end]:
            begin += 1
            end -= 1
        else:
            return False
    return True

#longest palindrom substring
def lps(s):
    begin = 0
    end = len(s) - 1
    sub = ''
    if len(s) == 0:
        return False
    elif len(s) == 1:
        return s
    elif len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return False
    while begin < end:
        if s[begin] != s[end]:
            end -= 1
        else:
            if palindrome(s[begin:end+1]):
                return s[begin:end+1]
    return False

# maximal difference
def md(A):
    return max(A) - min(A)


def partition_even_odd(A):
    begin = 0
    end = len(A) - 1
    while begin < end:
        if A[end] % 2 != 0:
            end -= 1
        if A[begin] % 2 == 0:
            begin += 1
        if A[begin] % 2 != 0 and A[end] % 2 == 0:
            A[begin], A[end] = A[end], A[begin]
            begin += 1
            end -= 1
    return A
        

def prime_factorize(n):
    assert n > 1
    # a**j * b**k == n
    # factorization is with prime numbers elevated to some power
    prime_factors = []
    while n % 2 == 0:
        n = n // 2
        prime_factors.append(2)
        if n == 1:
            break
    for factor in range(3, n+1):
        while n % factor == 0:
            n = n // factor
            prime_factors.append(factor)
            if n == 1:
                break

    factors = {}
    for number in prime_factors:
        if number in factors:
            factors[number] += 1
        else:
            factors[number] = 1
    print(factors)

    for key,value in factors.items():
        if value == 1:
            print(key)
        else:
            print(f'{key}E{value}')
