def is_sorted(A):
    direction = 0
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            if direction > 0:
                return False
            direction = -1
        elif A[i] > A[i-1]:
            if direction < 0:
                return False
            direction = 1
    return True