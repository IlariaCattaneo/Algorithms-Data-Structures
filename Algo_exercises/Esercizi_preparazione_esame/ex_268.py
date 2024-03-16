def find_avg_point(A):
    # we assert that A is already sorted in decreasing or increasing order
    if len(A) == 1:
        return 1
    m = (A[0] + A[len(A)-1])//2
    for i in range(len(A)-1):
        if A[i] <= m and A[i+1] >= m:
            return i
        elif A[i] >= m and A[i+1] <= m:
            return i