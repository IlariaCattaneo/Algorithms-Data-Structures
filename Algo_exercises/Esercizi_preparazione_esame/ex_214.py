def minimal_contiguous_sum(A):
    n = len(A)
    DP = [0]*n
    DP[0] = A[0]
    for i in range(1, n):
        DP[i] = min(A[i], DP[i-1]+A[i])
    min_sum = 0
    for number in DP:
        if number < min_sum:
            min_sum = number
    return min_sum