def exact_sum(A, B, t):
    # A is sorted, B is is sorted
    i = 0
    j = len(B) - 1
    while i < len(A) and j >= 0:
        if A[i] + B[j] < t:
            i += 1
        elif A[i] + B[j] > t:
            j -= 1
        else:
            return True
    return False