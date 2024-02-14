def maximal_increasing_subsequence(A):
    c = 1
    maxc = 0
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            c += 1
            if c > maxc:
                maxc = c
        elif A[i] >= A[i+1]:
            c = 1
    print(maxc)