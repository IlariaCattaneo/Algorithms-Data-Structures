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