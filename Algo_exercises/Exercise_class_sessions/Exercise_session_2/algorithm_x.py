def is_monotonic(A, i, j):
    increasing = True
    decreasing = True
    for a in range(i, j):
        if A[a] < A[a+1]:
            decreasing = False
        elif A[a] > A[a+1]:
            increasing = False
        if increasing == False and decreasing == False:
            return False
    return True

def algorithm_x(A):
    x = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if is_monotonic(A, i, j):
                if x < j - i:
                    x = j - i
    return x

def linear_algorithm_x(A):
    if len(A) == 0:
        return 0
    m = 1
    begin = 0                   # first check non-decreasing subsequences
    for i in range (1, len(A)):
        if A[i-1] > A[i]:
            begin = i
        if i - begin + 1 > m:
            m = i - begin + 1
    begin = 0                   # then check non-increasing subsequences
    for i in range (1, len(A)):
        if A[i-1] < A[i]:
            begin = i
        if i - begin + 1 > m:
            m = i - begin + 1
    return m

def better_algorithm_x(A):
    return linear_algorithm_x(A)