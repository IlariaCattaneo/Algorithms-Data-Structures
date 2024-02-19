def is_sorted(A):
    increasing = True
    decreasing = True
    for i in range(len(A)-1):
        if (A[i] < A[i+1] and not(increasing)) or (A[i] > A[i+1] and not(decreasing)):
            return False
        elif A[i] < A[i+1]:
            decreasing = False
        elif A[i] > A[i+1]:
            increasing = False
    return True
