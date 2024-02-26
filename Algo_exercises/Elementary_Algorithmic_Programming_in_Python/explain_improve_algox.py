def is_monotonic(A, i, j):
    assert i <= j and j < len(A)
    direction = 0
    for k in range(i, j):
        if A[k] < A[k+1]:
            if direction == -1:
                return False
            direction = 1
        elif A[k] > A[k+1]:
            if direction == 1:
                return False
            direction = -1
    return True

def algorithm_x (A):
    x = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if is_monotonic (A, i, j):
                if x < j - i:
                    x = j - i
    return x

# question 1
# the function algorithm_x returns the maximal lenght of any monotonic subsequence of A

# question 2
# since the function is_monotonic scans the subsequence of an array, its worst case complexity is O(n) when the length of the subsequence is equal to the length of the array
# the function algorithm_x scans the array to check any monotonic subsequence; given that inside the function we call function is_monotonic, then the worst case complexity is O(n^3)

# question 3-4
def linear_algorithm_x(A):
    if len(A) < 2:
        return len(A)
    x = 0
    direction = 0
    j = 0
    for i in range(1,len(A)):
        if A[i] > A[i-1]:
            if direction < 0:
                j = i
            direction = 1
        elif A[i] < A[i-1]:
            if direction > 0:
                j = i
            direction = -1
        if x < i - j + 1:
            x = i - j + 1
    return x

